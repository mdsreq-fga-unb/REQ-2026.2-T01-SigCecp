"""Ajustes para o ambiente de produção (issues #81, #83 e #85)."""
from sqlalchemy import text

from backend.database import engine
from backend.main import MEDIA_DIR, _rotas_documentacao


def test_pasta_de_midias_existe_ao_importar_a_aplicacao():
    assert MEDIA_DIR.is_dir()


def test_sqlite_verifica_chaves_estrangeiras():
    with engine.connect() as conexao:
        assert conexao.execute(text("PRAGMA foreign_keys")).scalar() == 1


def test_documentacao_da_api_desligada_em_producao(monkeypatch):
    monkeypatch.setenv("APP_ENV", "production")
    assert _rotas_documentacao() == {"docs_url": None, "redoc_url": None, "openapi_url": None}


def test_documentacao_da_api_disponivel_em_desenvolvimento(monkeypatch):
    monkeypatch.setenv("APP_ENV", "development")
    assert _rotas_documentacao() == {}
