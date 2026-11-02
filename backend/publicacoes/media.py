
import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


DIRETORIO_BASE = Path(__file__).resolve().parents[1] / "media"
DIRETORIO_PUBLICACOES = DIRETORIO_BASE / "publicacoes"

TIPOS_IMAGEM = {
    "image/jpeg",
    "image/png",
    "image/webp",
}

TIPOS_VIDEO = {
    "video/mp4",
    "video/webm",
    "video/ogg",
    "video/quicktime",
}


def salvar_midia(
    arquivo: UploadFile | None,
    tipos_permitidos: set[str],
) -> str | None:

    if arquivo is None or not arquivo.filename:
        return None

    if arquivo.content_type not in tipos_permitidos:
        raise ValueError(
            f"Formato não permitido: {arquivo.content_type}"
        )

    DIRETORIO_PUBLICACOES.mkdir(
        parents=True,
        exist_ok=True,
    )

    extensao = Path(arquivo.filename).suffix.lower()
    nome_arquivo = f"{uuid4().hex}{extensao}"

    caminho = DIRETORIO_PUBLICACOES / nome_arquivo

    with caminho.open("wb") as destino:
        shutil.copyfileobj(arquivo.file, destino)

    return f"publicacoes/{nome_arquivo}"


def remover_midia(caminho: str | None) -> None:

    if not caminho:
        return

    arquivo = (DIRETORIO_BASE / caminho).resolve()

    if not arquivo.is_relative_to(DIRETORIO_BASE.resolve()):
        return

    if arquivo.is_file():
        arquivo.unlink()
