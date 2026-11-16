import hashlib
import secrets
from datetime import datetime
from functools import lru_cache

import bcrypt
from jose import JWTError, jwt

from backend.auth import settings as cfg
from backend.auth.tempo import agora


SENHA_TAMANHO_MINIMO = 8
BCRYPT_MAX_BYTES = 72


class SenhaInvalida(ValueError):
    """A senha não atende à política de criação"""


def validar_politica_senha(senha: str, usuario: str | None = None) -> None:
    if "\x00" in senha:
        raise SenhaInvalida("A senha não pode conter o caractere nulo.")
    if len(senha) < SENHA_TAMANHO_MINIMO:
        raise SenhaInvalida(f"A senha deve ter pelo menos {SENHA_TAMANHO_MINIMO} caracteres.")
    if len(senha.encode("utf-8")) > BCRYPT_MAX_BYTES:
        raise SenhaInvalida(
            f"A senha deve ter no máximo {BCRYPT_MAX_BYTES} bytes em UTF-8 (limite do bcrypt)."
        )
    if usuario and senha.casefold() == usuario.casefold():
        raise SenhaInvalida("A senha não pode ser igual ao usuário.")


def gerar_hash(senha: str) -> str:
    salt = bcrypt.gensalt(rounds=cfg.settings.bcrypt_rounds)
    return bcrypt.hashpw(senha.encode("utf-8"), salt).decode("ascii")


def hash_senha(senha: str) -> str:
    validar_politica_senha(senha)
    return gerar_hash(senha)


def verificar_senha(senha: str, senha_hash: str) -> bool:
    dados = senha.encode("utf-8")
    if len(dados) > BCRYPT_MAX_BYTES or b"\x00" in dados:
        return False
    try:
        return bcrypt.checkpw(dados, senha_hash.encode("ascii"))
    except (ValueError, UnicodeEncodeError):
        return False


def hash_precisa_atualizar(senha_hash: str) -> bool:
    try:
        custo = int(senha_hash.split("$")[2])
    except (IndexError, ValueError):
        return True
    return custo < cfg.settings.bcrypt_rounds


@lru_cache(maxsize=1)
def _hash_ficticio() -> str:
    return bcrypt.hashpw(secrets.token_bytes(16), bcrypt.gensalt(rounds=cfg.settings.bcrypt_rounds)).decode("ascii")


def gastar_tempo_de_verificacao() -> None:
    bcrypt.checkpw(b"senha-ficticia", _hash_ficticio().encode("ascii"))


def criar_access_token(admin_id: int, sid: str) -> tuple[str, datetime]:
    s = cfg.settings
    emitido = agora()
    expira = emitido + s.access_ttl
    claims = {
        "sub": str(admin_id),
        "sid": sid,
        "typ": "access",
        "iss": s.jwt_emissor,
        "aud": s.jwt_audiencia,
        "iat": int(emitido.timestamp()),
        "exp": int(expira.timestamp()),
        "jti": secrets.token_hex(8),
    }
    return jwt.encode(claims, s.jwt_key, algorithm=s.jwt_algoritmo), expira


def decodificar_access_token(token: str) -> dict | None:
    s = cfg.settings
    try:
        claims = jwt.decode(
            token,
            s.jwt_key,
            algorithms=[s.jwt_algoritmo],
            audience=s.jwt_audiencia,
            issuer=s.jwt_emissor,
            options={"require_exp": True, "require_iat": True, "require_sub": True,
                     "require_iss": True, "require_aud": True},
        )
    except JWTError:
        return None
    if claims.get("typ") != "access":
        return None
    sid, sub = claims.get("sid"), claims.get("sub")
    if not isinstance(sid, str) or not isinstance(sub, str) or not sub.isdigit():
        return None
    return claims


def novo_refresh_token() -> str:
    return secrets.token_urlsafe(48)


def hash_token(token: str) -> str:
    return hashlib.sha256(token.encode("utf-8")).hexdigest()
