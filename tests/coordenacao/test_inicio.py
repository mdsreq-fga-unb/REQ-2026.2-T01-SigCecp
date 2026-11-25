"""Central da coordenação (backend/coordenacao/router.py)."""
import pytest
from fastapi.testclient import TestClient

from backend.auth.csrf import verificar_csrf
from backend.auth.dependencies import exigir_admin
from backend.main import app


@pytest.fixture
def cliente():
    app.dependency_overrides[exigir_admin] = lambda: object()
    app.dependency_overrides[verificar_csrf] = lambda: None
    try:
        with TestClient(app, follow_redirects=False) as cliente:
            yield cliente
    finally:
        app.dependency_overrides.clear()


def test_central_mostra_as_quatro_areas_e_suas_acoes(cliente):
    resposta = cliente.get("/coordenacao")

    assert resposta.status_code == 200
    html = resposta.text.replace("http://testserver", "")
    assert "Central da coordenação" in html
    for area in ("Conteúdos institucionais", "Eventos", "Alunos", "Turmas"):
        assert area in html
    for destino in ("/coordenacao/conteudo/novo", "/coordenacao/eventos/novo", "/coordenacao/alunos/novo", "/coordenacao/turmas/novo"):
        assert f'href="{destino}"' in html


def test_menu_nao_tem_item_inicio(cliente):
    html = cliente.get("/coordenacao").text
    menu = html.split('aria-label="Áreas da coordenação"', 1)[1].split("</nav>", 1)[0]

    assert "Início" not in menu


def test_central_exige_login(cliente):
    del app.dependency_overrides[exigir_admin]

    assert cliente.get("/coordenacao").status_code in (302, 303, 401)


def test_cada_area_tem_so_criar_e_ver_a_lista(cliente):
    html = cliente.get("/coordenacao").text

    for atalho in ("Ver conteúdos publicados", "Ver eventos publicados", "Ver alunos", "Ver turmas"):
        assert atalho in html
    for antigo in ("Editar conteúdo", "Remover evento", "Inativar aluno", "Associar aluno à turma"):
        assert antigo not in html
