import os
from pathlib import Path
from tempfile import TemporaryDirectory

import pytest


# backend.database cria o engine ao ser importado durante a coleta dos testes.
_database_directory = TemporaryDirectory(prefix="sigcecp-pytest-")
_database_path = Path(_database_directory.name) / "coleta.db"
os.environ["DATABASE_URL"] = f"sqlite:///{_database_path.as_posix()}"

# backend.main monta /media com StaticFiles, que exige o diretório existente.
# Ele está no .gitignore, então não existe em um clone limpo nem na CI.
(Path(__file__).resolve().parents[1] / "backend" / "media").mkdir(exist_ok=True)


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


@pytest.fixture
def novo_upload():
    """Fábrica de UploadFile em memória, como os recebidos pelos formulários."""
    from io import BytesIO

    from fastapi import UploadFile
    from starlette.datastructures import Headers

    def criar(nome="foto.png", tipo="image/png", conteudo=b"conteudo"):
        return UploadFile(
            file=BytesIO(conteudo),
            filename=nome,
            headers=Headers({"content-type": tipo}),
        )

    return criar


@pytest.fixture
def pasta_midias(tmp_path, monkeypatch) -> Path:
    """Redireciona as mídias de publicações para uma pasta temporária."""
    from backend.publicacoes import media

    base = tmp_path / "media"
    monkeypatch.setattr(media, "DIRETORIO_BASE", base)
    monkeypatch.setattr(media, "DIRETORIO_PUBLICACOES", base / "publicacoes")
    return base