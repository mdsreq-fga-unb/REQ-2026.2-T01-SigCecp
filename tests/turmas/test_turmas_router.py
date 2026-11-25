"""Rotas e páginas de turmas e da associação de alunos (backend/turmas/router.py)."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import backend.auth.models  # noqa: F401  (registra as tabelas de autenticação)
from backend.auth.csrf import verificar_csrf
from backend.auth.dependencies import exigir_admin
from backend.database import Base, get_db
from backend.main import app
from backend.turmas.models import Turma

BASE = "/coordenacao/turmas"


@pytest.fixture
def ambiente(tmp_path):
    engine = create_engine(
        f"sqlite:///{(tmp_path / 'turmas.db').as_posix()}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    sessoes = sessionmaker(bind=engine, autoflush=False)

    def sessao_temporaria():
        with sessoes() as db:
            yield db

    app.dependency_overrides[get_db] = sessao_temporaria
    app.dependency_overrides[exigir_admin] = lambda: object()
    app.dependency_overrides[verificar_csrf] = lambda: None
    try:
        with TestClient(app, follow_redirects=False) as cliente:
            yield cliente, sessoes
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def formulario(**alteracoes):
    dados = {"modalidade": "Judô", "dias": ["segunda", "quarta"], "inicio": "14:00", "termino": "15:00"}
    dados.update(alteracoes)
    return dados


def cadastrar(cliente, **alteracoes):
    resposta = cliente.post(f"{BASE}/novo", data=formulario(**alteracoes))
    assert resposta.status_code == 303
    return resposta


def turmas_no_banco(sessoes):
    with sessoes() as db:
        return db.query(Turma).order_by(Turma.id).all()


# ---------- Consultar ----------

def test_lista_vazia(ambiente):
    cliente, _ = ambiente

    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert "Cadastre a primeira turma" in resposta.text


def test_lista_mostra_turma_e_link_para_ver_alunos(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert "Judô" in resposta.text
    assert "Cadastre a primeira turma" not in resposta.text
    assert "1 turma cadastrada" in resposta.text
    assert "0 alunos" in resposta.text
    assert f'{BASE}/{turma_id}/alunos"' in resposta.text


# ---------- Cadastrar ----------

def test_pagina_de_cadastro(ambiente):
    cliente, _ = ambiente

    resposta = cliente.get(f"{BASE}/novo")

    assert resposta.status_code == 200
    assert 'name="modalidade"' in resposta.text


def test_cadastrar_redireciona_para_a_lista_e_grava(ambiente):
    cliente, sessoes = ambiente

    resposta = cadastrar(cliente)

    assert resposta.headers["location"].endswith(BASE)
    [turma] = turmas_no_banco(sessoes)
    assert turma.modalidade == "Judô"
    assert turma.dias == ["segunda", "quarta"]


@pytest.mark.parametrize(
    "invalido",
    [{"modalidade": ""}, {"dias": []}, {"dias": ["feriado"]}, {"inicio": "não é hora"}],
)
def test_cadastrar_com_dados_invalidos_e_recusado(ambiente, invalido):
    cliente, sessoes = ambiente

    resposta = cliente.post(f"{BASE}/novo", data=formulario(**invalido))

    assert resposta.status_code == 422
    assert turmas_no_banco(sessoes) == []


def test_cadastrar_turma_repetida_retorna_409(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)

    resposta = cliente.post(f"{BASE}/novo", data=formulario())

    assert resposta.status_code == 409
    assert len(turmas_no_banco(sessoes)) == 1


# ---------- Editar ----------

def test_pagina_de_edicao_vem_preenchida(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente, modalidade="Capoeira")
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.get(f"{BASE}/{turma_id}/editar")

    assert resposta.status_code == 200
    assert "Capoeira" in resposta.text


def test_editar_grava_e_redireciona(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.post(
        f"{BASE}/{turma_id}/editar",
        data=formulario(modalidade="Judô infantil", dias=["sabado"]),
    )

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith(BASE)
    [turma] = turmas_no_banco(sessoes)
    assert turma.modalidade == "Judô infantil"
    assert turma.dias == ["sabado"]


def test_editar_para_turma_repetida_retorna_409(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente, modalidade="Judô")
    cadastrar(cliente, modalidade="Capoeira")
    outra_id = turmas_no_banco(sessoes)[1].id

    resposta = cliente.post(f"{BASE}/{outra_id}/editar", data=formulario(modalidade="Judô"))

    assert resposta.status_code == 409


# ---------- Remover ----------

def test_get_de_remocao_so_confirma(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.get(f"{BASE}/{turma_id}/remover")

    assert resposta.status_code == 200
    assert "Judô" in resposta.text
    assert len(turmas_no_banco(sessoes)) == 1


def test_remover_desativa_e_redireciona(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.post(f"{BASE}/{turma_id}/remover")

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith(BASE)
    [turma] = turmas_no_banco(sessoes)
    assert turma.ativa is False
    assert "Cadastre a primeira turma" in cliente.get(BASE).text


@pytest.mark.parametrize("caminho", ["/editar", "/remover", "/alunos", "/alunos/associar"])
def test_turma_removida_nao_e_mais_acessada(ambiente, caminho):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id
    cliente.post(f"{BASE}/{turma_id}/remover")

    assert cliente.get(f"{BASE}/{turma_id}{caminho}").status_code == 404


def test_turma_removida_nao_impede_cadastrar_outra_igual(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    cliente.post(f"{BASE}/{turmas_no_banco(sessoes)[0].id}/remover")

    cadastrar(cliente)

    assert [t.ativa for t in turmas_no_banco(sessoes)] == [False, True]


# ---------- Ver alunos associados ----------

def test_ver_alunos_mostra_turma_sem_alunos(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.get(f"{BASE}/{turma_id}/alunos")

    assert resposta.status_code == 200
    assert "Alunos da turma" in resposta.text
    assert "Judô" in resposta.text
    assert "Nenhum aluno associado a esta turma ainda." in resposta.text


# ---------- Associar alunos ----------

def test_pagina_de_associar(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.get(f"{BASE}/{turma_id}/alunos/associar")

    assert resposta.status_code == 200
    html = resposta.text
    assert "Associar aluno à turma" in html
    assert 'name="aluno_id"' in html
    assert "Nenhum aluno disponível" in html
    assert "Judô • Segunda e quarta-feira • 14h às 15h" in html
    assert f'action="{BASE}/{turma_id}/alunos"' in html.replace("http://testserver", "")
    for campo in ("resumo-modalidade", "resumo-dias", "resumo-horario"):
        assert f'id="{campo}"' in html


def test_associar_lista_todas_as_turmas_e_marca_a_da_url(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente, modalidade="Judô")
    cadastrar(cliente, modalidade="Capoeira", dias=["sabado"], inicio="09:30", termino="11:00")
    judo, capoeira = turmas_no_banco(sessoes)

    resposta = cliente.get(f"{BASE}/{capoeira.id}/alunos/associar")

    html = resposta.text
    assert "Judô • Segunda e quarta-feira • 14h às 15h" in html
    assert "Capoeira • Sábado • 9h30 às 11h" in html
    def abertura_da_opcao(turma_id):
        return html.split(f'<option value="{turma_id}"', 1)[1].split(">", 1)[0]

    assert "selected" in abertura_da_opcao(capoeira.id)
    assert "selected" not in abertura_da_opcao(judo.id)


def test_dias_em_sequencia_usam_virgula_e_e(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente, dias=["sexta", "segunda", "quarta"])
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.get(f"{BASE}/{turma_id}/alunos/associar")

    assert "Segunda, quarta e sexta-feira" in resposta.text


def test_confirmar_associacao_sem_aluno_pede_o_aluno(ambiente):
    cliente, sessoes = ambiente
    cadastrar(cliente)
    turma_id = turmas_no_banco(sessoes)[0].id

    resposta = cliente.post(f"{BASE}/{turma_id}/alunos", data={"turma_id": turma_id})

    assert resposta.status_code == 422
    assert "Selecione o aluno que será associado à turma." in resposta.text


# ---------- Turma inexistente ----------

@pytest.mark.parametrize(
    "metodo, caminho",
    [
        ("get", "/99/editar"),
        ("get", "/99/remover"),
        ("post", "/99/remover"),
        ("get", "/99/alunos"),
        ("get", "/99/alunos/associar"),
        ("post", "/99/alunos"),
    ],
)
def test_turma_inexistente_retorna_404(ambiente, metodo, caminho):
    cliente, _ = ambiente

    resposta = getattr(cliente, metodo)(f"{BASE}{caminho}")

    assert resposta.status_code == 404


# ---------- Proteção ----------

@pytest.mark.parametrize(
    "caminho",
    ["", "/novo", "/1/editar", "/1/remover", "/1/alunos", "/1/alunos/associar"],
)
def test_rotas_exigem_login(ambiente, caminho):
    cliente, _ = ambiente
    del app.dependency_overrides[exigir_admin]

    resposta = cliente.get(f"{BASE}{caminho}")

    assert resposta.status_code in (302, 303, 401)
