import shutil
from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

DIRETORIO_EVENTOS = Path("backend/media/eventos")

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
        raise ValueError("Formato de arquivo não permitido.")

    DIRETORIO_EVENTOS.mkdir(parents=True, exist_ok=True)

    extensao = Path(arquivo.filename).suffix.lower()
    nome_arquivo = f"{uuid4().hex}{extensao}"

    caminho = DIRETORIO_EVENTOS / nome_arquivo

    with caminho.open("wb") as destino:
        shutil.copyfileobj(arquivo.file, destino)

    return f"eventos/{nome_arquivo}"


def remover_midia(caminho: str | None) -> None:
    if not caminho:
        return

    arquivo = Path("backend/media") / caminho

    if arquivo.is_file():
        arquivo.unlink()