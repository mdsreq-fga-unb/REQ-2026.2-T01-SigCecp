"""Armazenamento dos documentos do aluno, cifrados e fora da pasta pública /media (RNF12)."""
from pathlib import Path
from uuid import uuid4

from backend.cripto import cifrar, decifrar

DIRETORIO_ARQUIVOS = Path(__file__).resolve().parents[1] / "arquivos" / "alunos"


def gravar_arquivo(conteudo: bytes) -> str:
    DIRETORIO_ARQUIVOS.mkdir(parents=True, exist_ok=True)
    nome = f"{uuid4().hex}.bin"
    (DIRETORIO_ARQUIVOS / nome).write_bytes(cifrar(conteudo))
    return nome


def ler_arquivo(nome: str) -> bytes:
    caminho = (DIRETORIO_ARQUIVOS / nome).resolve()
    if not caminho.is_relative_to(DIRETORIO_ARQUIVOS.resolve()) or not caminho.is_file():
        raise FileNotFoundError(nome)
    return decifrar(caminho.read_bytes())
