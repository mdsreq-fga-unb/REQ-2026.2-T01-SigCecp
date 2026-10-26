from datetime import date, time
from decimal import Decimal

import pytest
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from backend.eventos.models import Evento
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import (
    buscar_evento_por_id,
    criar_evento,
    listar_eventos,
)


@pytest.fixture
def sessoes(tmp_path):
    engine = create_engine(f"sqlite:///{(tmp_path / 'eventos.db').as_posix()}", poolclass=NullPool)
    Evento.__table__.create(engine)
    yield sessionmaker(bind=engine)
    engine.dispose()


def test_criar_evento_gratuito_e_ler_em_nova_sessao(sessoes, dados_evento):
    with sessoes() as db:
        evento = criar_evento(db, EventoCreate(**dados_evento))
        evento_id = evento.id

    with sessoes() as db:
        encontrado = buscar_evento_por_id(db, evento_id)

        assert encontrado is not None
        assert encontrado.id == evento_id
        assert encontrado.titulo == dados_evento["titulo"]
        assert encontrado.cobrado is False
        assert encontrado.alimentacao is False
        assert encontrado.valor is None
        assert encontrado.data == date(2026, 11, 15)
        assert encontrado.inicio == time(9)
        assert encontrado.termino == time(12)


def test_criar_evento_pago_preserva_valor_e_datas(sessoes, dados_evento):
    dados = EventoCreate(**{
        **dados_evento, "cobrado": True, "valor": "25.50",
        "data_limite_pagamento": "2026-11-10", "meio_pagamento": "PIX",
    })
    with sessoes() as db:
        evento_id = criar_evento(db, dados).id

    with sessoes() as db:
        encontrado = buscar_evento_por_id(db, evento_id)

        assert encontrado.cobrado is True
        assert encontrado.valor == Decimal("25.50")
        assert isinstance(encontrado.valor, Decimal)
        assert encontrado.data_limite_pagamento == date(2026, 11, 10)
        assert encontrado.meio_pagamento == "PIX"


def test_lista_vazia_e_busca_inexistente(sessoes):
    with sessoes() as db:
        assert listar_eventos(db) == []
        assert buscar_evento_por_id(db, 999) is None


def test_lista_ordenada_por_data_inicio_e_id(sessoes, dados_evento):
    with sessoes() as db:
        ultimo = criar_evento(db, EventoCreate(**dados_evento)).id
        meio = criar_evento(db, EventoCreate(**{
            **dados_evento, "data": "2026-11-10", "inicio": "10:00",
        })).id
        primeiro = criar_evento(db, EventoCreate(**{
            **dados_evento, "data": "2026-11-10", "inicio": "09:00",
        })).id
        empate = criar_evento(db, EventoCreate(**{
            **dados_evento, "data": "2026-11-10", "inicio": "09:00",
        })).id

    with sessoes() as db:
        assert [evento.id for evento in listar_eventos(db)] == [
            primeiro, empate, meio, ultimo,
        ]


def test_falha_real_faz_rollback_e_sessao_pode_ser_reutilizada(sessoes, dados_evento):
    with sessoes() as db:
        with db.bind.begin() as connection:
            connection.exec_driver_sql(
                "CREATE TRIGGER recusar_evento BEFORE INSERT ON eventos "
                "WHEN NEW.titulo = 'Recusar' "
                "BEGIN SELECT RAISE(ABORT, 'falha de gravacao'); END"
            )

    with sessoes() as db:
        with pytest.raises(IntegrityError, match="falha de gravacao"):
            criar_evento(db, EventoCreate(**{**dados_evento, "titulo": "Recusar"}))

        assert db.is_active
        evento_id = criar_evento(db, EventoCreate(**{
            **dados_evento, "titulo": "Após rollback",
        })).id

    with sessoes() as db:
        assert [evento.titulo for evento in listar_eventos(db)] == ["Após rollback"]
        assert buscar_evento_por_id(db, evento_id) is not None
