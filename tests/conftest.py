import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


# backend.database cria o engine ao ser importado durante a coleta dos testes.
_database_directory = TemporaryDirectory(prefix="sigcecp-pytest-")
_database_path = Path(_database_directory.name) / "coleta.db"
os.environ["DATABASE_URL"] = f"sqlite:///{_database_path.as_posix()}"


def pytest_unconfigure() -> None:
    _database_directory.cleanup()


@pytest.fixture
def dados_evento() -> dict:
    return {
        "titulo": "Festival CECP",
        "subtitulo": "Esporte para todos",
        "nome": "Festival esportivo",
        "data": "2026-11-15",
        "inicio": "09:00",
        "termino": "12:00",
        "local": "Quadra CECP",
        "descricao": "Atividades para a comunidade.",
        "alimentacao": False,
        "pesagem": "nao_se_aplica",
        "cobrado": False,
    }
