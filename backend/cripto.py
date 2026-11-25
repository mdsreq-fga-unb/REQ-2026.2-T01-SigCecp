"""Criptografia dos dados sensíveis do aluno (RNF12): dados de saúde e documentos anexados."""
import logging
import os
from pathlib import Path

from cryptography.fernet import Fernet
from sqlalchemy import Text
from sqlalchemy.types import TypeDecorator

logger = logging.getLogger("sigcecp.cripto")

# Em desenvolvimento, sem DADOS_CHAVE, a chave fica neste arquivo (está no .gitignore).
# Ela não pode ser efêmera: sem a mesma chave, os dados gravados não podem ser lidos de novo.
ARQUIVO_CHAVE_DEV = Path(__file__).resolve().parent / ".chave_dados_dev"

_fernet: Fernet | None = None


def _carregar_chave() -> bytes:
    chave = os.getenv("DADOS_CHAVE", "").strip()
    if chave:
        return chave.encode()

    if os.getenv("APP_ENV", "development").strip().lower() == "production":
        raise RuntimeError(
            "DADOS_CHAVE é obrigatória em produção (APP_ENV=production). Gere uma com: "
            "python -c \"from cryptography.fernet import Fernet; print(Fernet.generate_key().decode())\""
        )

    if not ARQUIVO_CHAVE_DEV.exists():
        ARQUIVO_CHAVE_DEV.write_bytes(Fernet.generate_key())
        logger.warning(
            "DADOS_CHAVE não definida: chave de desenvolvimento criada em %s. "
            "Defina DADOS_CHAVE no .env antes de usar dados reais.",
            ARQUIVO_CHAVE_DEV,
        )
    return ARQUIVO_CHAVE_DEV.read_bytes().strip()


def _cifra() -> Fernet:
    global _fernet
    if _fernet is None:
        _fernet = Fernet(_carregar_chave())
    return _fernet


def cifrar(dados: bytes) -> bytes:
    return _cifra().encrypt(dados)


def decifrar(dados: bytes) -> bytes:
    return _cifra().decrypt(dados)


class TextoCifrado(TypeDecorator):
    """Texto gravado cifrado no banco e devolvido em claro para a aplicação."""

    impl = Text
    cache_ok = True

    def process_bind_param(self, valor, dialect):
        if valor is None:
            return None
        return cifrar(valor.encode()).decode()

    def process_result_value(self, valor, dialect):
        if valor is None:
            return None
        return decifrar(valor.encode()).decode()
