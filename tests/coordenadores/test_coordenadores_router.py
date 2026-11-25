"""Criação de coordenador pelo Root (backend/coordenadores/router.py)."""
from types import SimpleNamespace

import pytest
from fastapi import Request
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.auth import security
from backend.auth.csrf import verificar_csrf
from backend.auth.dependencies import exigir_admin
from backend.auth.models import Administrador
from backend.auth.services import criar_administrador
from backend.database import Base, get_db
from backend.main import app

BASE = "/coordenacao/coordenadores"
SENHA = "Judo#2026cecp"


@pytest.fixture
def ambiente(tmp_path):
    engine = create_engine(
        f"sqlite:///{(tmp_path / 'contas.db').as_posix()}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    sessoes = sessionmaker(bind=engine, autoflush=False)

    def sessao_temporaria():
        with sessoes() as db:
            yield db

    app.dependency_overrides[get_db] = sessao_temporaria
    app.dependency_overrides[exigir_admin] = lambda: SimpleNamespace(usuario="ROOT", perfil="root")
    app.dependency_overrides[verificar_csrf] = lambda: None
    try:
        with TestClient(app, follow_redirects=False) as cliente:
            yield cliente, sessoes
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def formulario(**alteracoes):
    dados = {"nome": "Mariana Oliveira Santos", "usuario": "cecp0004", "senha": SENHA, "confirmar_senha": SENHA}
    dados.update(alteracoes)
    return dados


def contas(sessoes):
    with sessoes() as db:
        return db.query(Administrador).order_by(Administrador.id).all()


def test_pagina_de_criacao(ambiente):
    cliente, _ = ambiente

    resposta = cliente.get(f"{BASE}/novo")

    assert resposta.status_code == 200
    assert "Criar coordenador" in resposta.text
    assert 'type="password"' in resposta.text


def test_criar_coordenador_grava_perfil_coordenador_e_senha_com_hash(ambiente):
    cliente, sessoes = ambiente

    resposta = cliente.post(f"{BASE}/novo", data=formulario())

    assert resposta.status_code == 303
    [conta] = contas(sessoes)
    assert conta.nome == "Mariana Oliveira Santos"
    assert conta.usuario == "cecp0004"
    assert conta.perfil == "coordenador"
    assert conta.ativo
    assert SENHA not in conta.senha_hash
    assert security.verificar_senha(SENHA, conta.senha_hash)
    assert resposta.headers["location"].endswith(f"{BASE}/{conta.id}/criado")


def test_confirmacao_mostra_os_dados_sem_a_senha(ambiente):
    cliente, sessoes = ambiente
    cliente.post(f"{BASE}/novo", data=formulario())
    [conta] = contas(sessoes)

    html = cliente.get(f"{BASE}/{conta.id}/criado").text

    assert "Conta criada com sucesso" in html
    assert "cecp0004" in html
    assert SENHA not in html


def test_lista_mostra_so_coordenadores(ambiente):
    cliente, sessoes = ambiente
    with sessoes() as db:
        criar_administrador(db, "ROOT01", SENHA)
    cliente.post(f"{BASE}/novo", data=formulario())

    html = cliente.get(BASE).text

    assert "Mariana Oliveira Santos" in html
    assert "ROOT01" not in html
    assert "1 coordenador" in html


@pytest.mark.parametrize(
    "alteracao, mensagem",
    [
        ({"nome": ""}, "Informe o nome do coordenador."),
        ({"usuario": ""}, "Informe o usuário de acesso."),
        ({"confirmar_senha": "Outra#2026cecp"}, "As senhas não coincidem."),
        ({"senha": "curta", "confirmar_senha": "curta"}, "pelo menos 8 caracteres"),
    ],
)
def test_dados_invalidos_nao_criam_a_conta(ambiente, alteracao, mensagem):
    cliente, sessoes = ambiente

    resposta = cliente.post(f"{BASE}/novo", data=formulario(**alteracao))

    assert resposta.status_code == 422
    assert "Não foi possível criar a conta" in resposta.text
    assert mensagem in resposta.text
    assert SENHA not in resposta.text
    assert contas(sessoes) == []


def test_usuario_repetido_e_recusado(ambiente):
    cliente, sessoes = ambiente
    cliente.post(f"{BASE}/novo", data=formulario())

    resposta = cliente.post(f"{BASE}/novo", data=formulario(nome="Outra pessoa", usuario="CECP0004"))

    assert resposta.status_code == 422
    assert "Usuário já cadastrado" in resposta.text
    assert len(contas(sessoes)) == 1


@pytest.mark.parametrize("metodo, caminho", [("get", ""), ("get", "/novo"), ("post", "/novo"), ("get", "/1/criado")])
def test_coordenador_nao_acessa_a_area_do_root(ambiente, metodo, caminho):
    cliente, _ = ambiente
    app.dependency_overrides[exigir_admin] = lambda: SimpleNamespace(usuario="CECP0001", perfil="coordenador")

    resposta = getattr(cliente, metodo)(f"{BASE}{caminho}")

    assert resposta.status_code == 403


@pytest.mark.parametrize("caminho", ["", "/novo"])
def test_rotas_exigem_login(ambiente, caminho):
    cliente, _ = ambiente
    del app.dependency_overrides[exigir_admin]

    resposta = cliente.get(f"{BASE}{caminho}")

    assert resposta.status_code in (302, 303, 401)


def test_conta_criada_pelo_terminal_e_root(ambiente):
    _, sessoes = ambiente
    with sessoes() as db:
        conta = criar_administrador(db, "cecp0001", SENHA)

        assert conta.perfil == "root"


def test_selo_da_conta_leva_o_root_aos_coordenadores(ambiente):
    cliente, _ = ambiente

    def root_logado(request: Request):
        request.state.admin = SimpleNamespace(usuario="root", perfil="root")
        return request.state.admin

    app.dependency_overrides[exigir_admin] = root_logado

    html = cliente.get("/coordenacao/turmas").text

    assert f'class="usuario usuario--link" href="http://testserver{BASE}"' in html


def test_selo_da_conta_nao_e_link_para_coordenador(ambiente):
    cliente, _ = ambiente

    def coordenador_logado(request: Request):
        request.state.admin = SimpleNamespace(usuario="cecp0001", perfil="coordenador")
        return request.state.admin

    app.dependency_overrides[exigir_admin] = coordenador_logado

    html = cliente.get("/coordenacao/turmas").text

    assert "usuario--link" not in html
    assert f"{BASE}" not in html


def test_area_de_coordenadores_mostra_o_menu_das_funcoes(ambiente):
    cliente, _ = ambiente

    html = cliente.get(BASE).text
    menu = html.split('aria-label="Áreas da coordenação"', 1)[1].split("</nav>", 1)[0]

    for funcao in ("Conteúdos", "Eventos", "Alunos", "Turmas"):
        assert funcao in menu
    assert "Coordenadores" not in menu
    assert 'aria-current="page"' not in menu


@pytest.mark.parametrize("perfil", ["root", "coordenador"])
def test_login_leva_a_central_da_coordenacao(ambiente, perfil):
    cliente, sessoes = ambiente
    with sessoes() as db:
        criar_administrador(db, "cecp0009", SENHA, nome_completo="Conta de teste", perfil=perfil)

    resposta = cliente.post("/coordenacao/auth/login", data={"usuario": "CECP0009", "senha": SENHA})

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith("/coordenacao")
