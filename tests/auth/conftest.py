import re
from dataclasses import replace
from datetime import timedelta

import pytest
from fastapi.testclient import TestClient
from jose import jwt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend import database
from backend.auth import services
from backend.auth import settings as cfg
from backend.auth.tempo import agora
from backend.database import Base, get_db
from backend.main import app

USUARIO = "CECP0001"
SENHA = "senha-forte-123"


@pytest.fixture(autouse=True)
def config_de_teste(monkeypatch):
    nova = replace(
        cfg.settings,
        ambiente="test",
        secret_key="k" * 48,
        cookie_secure=False,
        cookie_samesite="strict",
        cookie_domain=None,
        bcrypt_rounds=4,
        login_max_tentativas=3,
        login_bloqueio=timedelta(minutes=15),
        access_ttl=timedelta(minutes=15),
        refresh_ttl=timedelta(days=7),
        sessao_max=timedelta(days=30),
        refresh_reuse_grace=timedelta(seconds=10),
        origens_confiaveis=frozenset(),
    )
    monkeypatch.setattr(cfg, "settings", nova)
    return nova


@pytest.fixture
def sessionmaker_teste(monkeypatch):
    engine = create_engine(
        "sqlite://",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    fabrica = sessionmaker(bind=engine, autoflush=False)

    def _get_db():
        db = fabrica()
        try:
            yield db
        finally:
            db.close()

    monkeypatch.setattr(database, "SessionLocal", fabrica)
    app.dependency_overrides[get_db] = _get_db
    yield fabrica
    app.dependency_overrides.pop(get_db, None)
    engine.dispose()


@pytest.fixture
def db(sessionmaker_teste):
    sessao = sessionmaker_teste()
    yield sessao
    sessao.close()


@pytest.fixture
def admin(db):
    return services.criar_administrador(db, USUARIO, SENHA)


@pytest.fixture
def client(sessionmaker_teste):
    with TestClient(app, follow_redirects=False) as c:
        yield c


# ---------- helpers ----------

def logar(client, usuario=USUARIO, senha=SENHA):
    return client.post(
        "/coordenacao/auth/login",
        data={"usuario": usuario, "senha": senha},
    )


def cookies_set(resposta) -> dict[str, str]:
    saida = {}
    for bruto in resposta.headers.get_list("set-cookie"):
        saida[bruto.split("=", 1)[0]] = bruto
    return saida


def token_csrf(client, caminho="/coordenacao/conteudo/novo") -> str:
    pagina = client.get(caminho)
    assert pagina.status_code == 200, pagina.text[:300]
    achou = re.search(r'name="csrf_token" value="([^"]+)"', pagina.text)
    assert achou, "campo csrf_token não encontrado na página"
    return achou.group(1)


def trocar_cookie(client, nome, valor):
    for c in client.cookies.jar:
        if c.name == nome:
            c.value = valor
            return
    raise AssertionError(f"cookie {nome} não está no jar")


def valor_cookie(client, nome):
    return next(c.value for c in client.cookies.jar if c.name == nome)


def access_com_expiracao(admin_id: int, sid: str, segundos: int) -> str:
    s = cfg.settings
    agora_ = agora()
    claims = {
        "sub": str(admin_id), "sid": sid, "typ": "access",
        "iss": s.jwt_emissor, "aud": s.jwt_audiencia,
        "iat": int((agora_ - timedelta(hours=1)).timestamp()),
        "exp": int((agora_ + timedelta(seconds=segundos)).timestamp()),
    }
    return jwt.encode(claims, s.jwt_key, algorithm=s.jwt_algoritmo)
