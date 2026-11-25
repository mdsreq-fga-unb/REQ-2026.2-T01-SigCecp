"""Erros mostrados ao navegador como página em português (backend/erros.py)."""
import re

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.auth.csrf import verificar_csrf
from backend.auth.dependencies import exigir_admin
from backend.database import Base, get_db
from backend.main import app

HTML = {"accept": "text/html"}


@pytest.fixture
def cliente(tmp_path):
    engine = create_engine(f"sqlite:///{(tmp_path / 'paginas.db').as_posix()}", connect_args={"check_same_thread": False})
    Base.metadata.create_all(engine)
    sessoes = sessionmaker(bind=engine)

    def sessao_temporaria():
        with sessoes() as db:
            yield db

    app.dependency_overrides[get_db] = sessao_temporaria
    app.dependency_overrides[exigir_admin] = lambda: object()
    app.dependency_overrides[verificar_csrf] = lambda: None
    try:
        with TestClient(app) as cliente:
            yield cliente
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def test_validacao_vira_pagina_com_os_campos(cliente):
    resposta = cliente.post("/coordenacao/turmas/novo", data={"modalidade": "", "inicio": "x"}, headers=HTML)

    assert resposta.status_code == 422
    assert "text/html" in resposta.headers["content-type"]
    problemas = re.findall(r"<li>([^<]*)</li>", resposta.text)
    assert "Dias: preencha este campo." in problemas
    assert "Horário de início: use um horário no formato 14:30." in problemas
    assert "Voltar e corrigir" in resposta.text


def test_pagina_inexistente_tem_mensagem_em_portugues(cliente):
    resposta = cliente.get("/nao-existe", headers=HTML)

    assert resposta.status_code == 404
    assert "Página não encontrada" in resposta.text
    assert 'href="/"' in resposta.text


def test_termino_antes_do_inicio_mostra_mensagem_clara(cliente):
    dados = {"modalidade": "Judô", "dias": ["segunda"], "inicio": "15:00", "termino": "14:00"}
    resposta = cliente.post("/coordenacao/turmas/novo", data=dados, headers=HTML)

    assert resposta.status_code == 422
    problemas = re.findall(r"<li>([^<]*)</li>", resposta.text)
    assert problemas == ["O horário de término deve ser depois do horário de início."]


def test_formularios_de_horario_carregam_a_conferencia(cliente):
    for pagina in ("/coordenacao/turmas/novo", "/coordenacao/eventos/novo"):
        assert "js/horarios.js" in cliente.get(pagina).text


def test_api_e_testes_continuam_recebendo_json(cliente):
    resposta = cliente.get("/nao-existe")

    assert resposta.status_code == 404
    assert resposta.json() == {"detail": "Not Found"}


# ---------- Itens de acessibilidade (NBR 17225 / WCAG 2.2) ----------

def test_tabelas_tem_legenda(cliente):
    cliente.post("/coordenacao/turmas/novo", data={"modalidade": "Judô", "dias": ["segunda"], "inicio": "14:00", "termino": "15:00"})

    assert "<caption" in cliente.get("/coordenacao/turmas").text
    assert "<caption" in cliente.get("/coordenacao/alunos").text


def test_opcoes_do_evento_sao_agrupadas(cliente):
    html = cliente.get("/coordenacao/eventos/novo").text

    assert html.count('role="radiogroup"') == 3


def test_lista_de_eventos_tem_titulo_proprio(cliente):
    assert "<title>Eventos | SigCECP</title>" in cliente.get("/eventos").text
