"""Testes de editar (RF18) e remover (RF19) evento.

Rodar:  pytest --cov=backend.eventos --cov-report=term-missing
"""
from datetime import date, time
from decimal import Decimal

from fastapi.staticfiles import StaticFiles
import pytest
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.config import ASSETS_DIR
from backend.database import Base, get_db
from backend.eventos.models import Evento
from backend.eventos.router import router
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import atualizar_evento


@pytest.fixture()
def db_session():
    engine = create_engine("sqlite://", connect_args={"check_same_thread": False},
                           poolclass=StaticPool)
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine, autoflush=False)()
    yield session
    session.close()


@pytest.fixture()
def client(db_session):
    app = FastAPI()
    app.mount("/static", StaticFiles(directory=ASSETS_DIR), name="static")
    app.include_router(router)

    @app.get("/eventos", name="modulo_eventos_publico")
    def _publico():
        return "ok"

    @app.get("/", name="modulo_conteudo_publico")
    def _inicio():
        return "ok"

    @app.get("/coordenacao/conteudo", name="lista_conteudo")
    def _lista_conteudo():
        return "ok"

    app.dependency_overrides[get_db] = lambda: db_session
    return TestClient(app, follow_redirects=False)


@pytest.fixture()
def evento(db_session):
    ev = Evento(
        titulo="Copa CECP", subtitulo="Etapa 1", nome="Campeonato Interno",
        data=date(2026, 11, 20), inicio=time(9, 0), termino=time(17, 0),
        local="Ginásio", descricao="Jiu-jitsu", alimentacao=True, pesagem="sim",
        cobrado=True, valor=Decimal("50.00"), data_limite_pagamento=date(2026, 11, 10),
        meio_pagamento="PIX",
    )
    db_session.add(ev)
    db_session.commit()
    return ev


DADOS = {
    "titulo": "Copa CECP 2026", "subtitulo": "Etapa final", "nome": "Campeonato Regional",
    "data": "2026-12-05", "inicio": "14:00", "termino": "18:30", "local": "Quadra 2",
    "descricao": "Final do ano", "alimentacao": "false", "pesagem": "nao_se_aplica",
    "cobrado": "false",
}


# ---------- RF18: editar ----------
def test_form_editar_vem_preenchido(client, evento):
    r = client.get(f"/coordenacao/eventos/{evento.id}/editar")
    assert r.status_code == 200
    assert "Copa CECP" in r.text and "Campeonato Interno" in r.text


def test_editar_salva_todos_os_campos_e_redireciona(client, evento, db_session):
    r = client.post(f"/coordenacao/eventos/{evento.id}/editar", data=DADOS)
    assert r.status_code == 303
    assert r.headers["location"].endswith("/eventos")
    db_session.refresh(evento)
    assert evento.titulo == "Copa CECP 2026" and evento.nome == "Campeonato Regional"
    assert evento.data == date(2026, 12, 5)
    assert (evento.inicio, evento.termino) == (time(14, 0), time(18, 30))
    assert evento.alimentacao is False and evento.pesagem == "nao_se_aplica"


def test_deixar_de_cobrar_limpa_dados_de_pagamento(client, evento, db_session):
    assert evento.valor == Decimal("50.00")
    client.post(f"/coordenacao/eventos/{evento.id}/editar", data=DADOS)  # cobrado=false, sem valor
    db_session.refresh(evento)
    assert evento.cobrado is False
    assert evento.valor is None and evento.meio_pagamento is None
    assert evento.data_limite_pagamento is None


def test_editar_mantendo_cobranca(client, evento, db_session):
    dados = {**DADOS, "cobrado": "true", "valor": "80.00",
             "data_limite_pagamento": "2026-11-30", "meio_pagamento": "Dinheiro"}
    client.post(f"/coordenacao/eventos/{evento.id}/editar", data=dados)
    db_session.refresh(evento)
    assert evento.valor == Decimal("80.00") and evento.meio_pagamento == "Dinheiro"


def test_editar_so_mexe_no_evento_certo(client, evento, db_session):
    outro = Evento(
        titulo="Outro", subtitulo="x", nome="Outro evento", data=date(2026, 12, 1),
        inicio=time(8, 0), termino=time(9, 0), local="Sala", descricao="d",
        alimentacao=False, pesagem="nao", cobrado=False,
    )
    db_session.add(outro); db_session.commit()
    client.post(f"/coordenacao/eventos/{evento.id}/editar", data=DADOS)
    db_session.refresh(outro)
    assert outro.nome == "Outro evento"


def test_editar_dados_invalidos_nao_salva(client, evento, db_session):
    dados = {k: v for k, v in DADOS.items() if k != "nome"}  # nome obrigatório ausente
    r = client.post(f"/coordenacao/eventos/{evento.id}/editar", data=dados)
    assert r.status_code == 422
    db_session.refresh(evento)
    assert evento.nome == "Campeonato Interno"


def test_editar_pesagem_invalida_nao_salva(client, evento):
    r = client.post(f"/coordenacao/eventos/{evento.id}/editar",
                    data={**DADOS, "pesagem": "talvez"})
    assert r.status_code == 422


def test_editar_evento_inexistente_404(client):
    assert client.get("/coordenacao/eventos/999/editar").status_code == 404
    assert client.post("/coordenacao/eventos/999/editar", data=DADOS).status_code == 404

def test_atualizar_ignora_campos_que_nao_existem_no_modelo(db_session, evento):
    class ComExtra(EventoCreate):
        foto: str = "x.png"

    dados = ComExtra(**{**DADOS, "data": date(2026, 12, 5), "inicio": time(14, 0),
                        "termino": time(18, 0), "alimentacao": False, "cobrado": False})
    atualizar_evento(db_session, evento.id, dados)
    
    colunas_banco = [c.name for c in Evento.__table__.columns]
    assert "foto" not in colunas_banco
# ---------- RF19: remover ----------
def test_tela_de_confirmacao_nao_apaga(client, evento, db_session):
    r = client.get(f"/coordenacao/eventos/{evento.id}/remover")
    assert r.status_code == 200 and "Remover evento?" in r.text
    assert db_session.get(Evento, evento.id) is not None

def test_remover_apos_confirmacao(client, evento, db_session):
    evento_id = evento.id
    r = client.post(f"/coordenacao/eventos/{evento_id}/remover")
    assert r.status_code == 303 and r.headers["location"].endswith("/eventos")
    db_session.expire_all()
    assert db_session.get(Evento, evento_id) is None
    assert client.get(f"/coordenacao/eventos/{evento_id}/editar").status_code == 404


def test_remover_evento_inexistente_404(client):
    assert client.get("/coordenacao/eventos/999/remover").status_code == 404
    assert client.post("/coordenacao/eventos/999/remover").status_code == 404