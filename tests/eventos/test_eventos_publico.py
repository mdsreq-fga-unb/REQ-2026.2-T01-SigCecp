from datetime import date, datetime, time, timezone

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.database import get_db
from backend.eventos.models import Evento
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import FUSO_BRASILIA, calcular_estado, criar_evento
from backend.main import app


@pytest.fixture
def consulta_publica(tmp_path):
    engine = create_engine(f"sqlite:///{(tmp_path / 'consulta.db').as_posix()}")
    Evento.__table__.create(engine)
    sessoes = sessionmaker(bind=engine)

    def sessao_temporaria():
        with sessoes() as db:
            yield db

    app.dependency_overrides[get_db] = sessao_temporaria
    try:
        with TestClient(app) as cliente:
            yield cliente, sessoes
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def criar_registro(sessoes, dados_evento, **alteracoes):
    with sessoes() as db:
        return criar_evento(db, EventoCreate(**{**dados_evento, **alteracoes})).id


def test_listagem_vazia(consulta_publica):
    cliente, _ = consulta_publica

    resposta = cliente.get("/eventos")

    assert resposta.status_code == 200
    assert "Nenhum evento publicado." in resposta.text
    assert "cartao-evento__titulo" not in resposta.text


def test_listagem_exibe_eventos_reais_e_links(consulta_publica, dados_evento):
    cliente, sessoes = consulta_publica
    primeiro_id = criar_registro(
        sessoes, dados_evento, titulo="Primeiro encontro", data="2026-11-10",
    )
    segundo_id = criar_registro(
        sessoes, dados_evento, titulo="Segundo encontro", data="2026-11-20",
    )

    resposta = cliente.get("/eventos")

    assert resposta.status_code == 200
    assert resposta.text.index("Primeiro encontro") < resposta.text.index("Segundo encontro")
    assert "10/11/2026" in resposta.text
    assert "Quadra CECP" in resposta.text
    assert f'/eventos/{primeiro_id}' in resposta.text
    assert f'/eventos/{segundo_id}' in resposta.text
    assert "2 eventos publicados." in resposta.text
    assert "Editar" not in resposta.text
    assert "Excluir" not in resposta.text


def test_detalhes_de_evento_pago(consulta_publica, dados_evento):
    cliente, sessoes = consulta_publica
    evento_id = criar_registro(
        sessoes, dados_evento, cobrado=True, valor="25.50",
        data_limite_pagamento="2026-11-10", meio_pagamento="PIX",
        alimentacao=True, pesagem="sim",
    )

    resposta = cliente.get(f"/eventos/{evento_id}")

    assert resposta.status_code == 200
    for conteudo in (
        "Festival CECP", "Esporte para todos", "Festival esportivo",
        "15/11/2026", "09:00", "12:00", "Quadra CECP",
        "Atividades para a comunidade.", "Alimentação", "Pesagem",
        "Evento cobrado", "R$ 25.50", "10/11/2026", "PIX",
    ):
        assert conteudo in resposta.text
    assert "Editar" not in resposta.text
    assert "Excluir" not in resposta.text


def test_detalhes_gratuitos_nao_exibem_pagamento(consulta_publica, dados_evento):
    cliente, sessoes = consulta_publica
    evento_id = criar_registro(
        sessoes, dados_evento, valor="0.00",
        data_limite_pagamento="2026-11-10", meio_pagamento="PIX",
    )

    resposta = cliente.get(f"/eventos/{evento_id}")

    assert resposta.status_code == 200
    assert "Gratuito" in resposta.text
    assert "Meio de pagamento" not in resposta.text
    assert "R$ 0.00" not in resposta.text
    assert "PIX" not in resposta.text
    assert "Editar" not in resposta.text
    assert "Excluir" not in resposta.text


def test_id_inexistente_retorna_404(consulta_publica):
    cliente, _ = consulta_publica

    resposta = cliente.get("/eventos/999999")

    assert resposta.status_code == 404


def test_listagem_mostra_os_tres_estados(consulta_publica, dados_evento, monkeypatch):
    class DataFixa(datetime):
        @classmethod
        def now(cls, tz=None):
            return cls(2026, 11, 15, 9, 30, tzinfo=tz)

    monkeypatch.setattr("backend.main.datetime", DataFixa)
    cliente, sessoes = consulta_publica
    criar_registro(sessoes, dados_evento, data="2026-11-14")
    criar_registro(sessoes, dados_evento, data="2026-11-15", inicio="09:00", termino="10:00")
    criar_registro(sessoes, dados_evento, data="2026-11-16")

    resposta = cliente.get("/eventos")

    assert resposta.status_code == 200
    assert resposta.text.count(">Em breve<") == 1
    assert resposta.text.count(">Em andamento<") == 1
    assert resposta.text.count(">Encerrado<") == 1


@pytest.mark.parametrize("instante, esperado", [
    (datetime(2026, 11, 15, 8, 59, 59, tzinfo=FUSO_BRASILIA), "Em breve"),
    (datetime(2026, 11, 15, 9, 0, tzinfo=FUSO_BRASILIA), "Em andamento"),
    (datetime(2026, 11, 15, 10, 0, tzinfo=FUSO_BRASILIA), "Em andamento"),
    (datetime(2026, 11, 15, 10, 0, 1, tzinfo=FUSO_BRASILIA), "Encerrado"),
])
def test_estados_e_limites(instante, esperado):
    evento = Evento(data=date(2026, 11, 15), inicio=time(9), termino=time(10))

    assert calcular_estado(evento, instante) == esperado


def test_estado_converte_instante_utc_para_brasilia():
    evento = Evento(data=date(2026, 11, 15), inicio=time(9), termino=time(10))
    agora_utc = datetime(2026, 11, 15, 12, 0, tzinfo=timezone.utc)

    assert calcular_estado(evento, agora_utc) == "Em andamento"


def test_instante_sem_fuso_e_rejeitado():
    evento = Evento(data=date(2026, 11, 15), inicio=time(9), termino=time(10))

    with pytest.raises(ValueError, match="fuso horário"):
        calcular_estado(evento, datetime(2026, 11, 15, 9, 0))
