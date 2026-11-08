"""Configuração da autenticação do administrador"""

import hashlib
import hmac
import logging
import os
import secrets
from dataclasses import dataclass
from datetime import timedelta
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent.parent
load_dotenv(BASE_DIR / ".env")

logger = logging.getLogger("sigcecp.auth")

AMBIENTES = {"development", "production", "test"}
SAMESITE_VALIDOS = {"strict", "lax", "none"}
TAMANHO_MINIMO_SEGREDO = 32


def _ler_bool(nome: str, padrao: bool) -> bool:
    bruto = os.getenv(nome)
    if bruto is None or not bruto.strip():
        return padrao
    valor = bruto.strip().lower()
    if valor in {"1", "true", "yes", "sim", "on"}:
        return True
    if valor in {"0", "false", "no", "nao", "não", "off"}:
        return False
    raise RuntimeError(f"{nome} deve ser 'true' ou 'false' (recebido: {bruto!r}).")


def _ler_int(nome: str, padrao: int, minimo: int = 1) -> int:
    bruto = os.getenv(nome)
    if bruto is None or not bruto.strip():
        return padrao
    try:
        valor = int(bruto.strip())
    except ValueError:
        raise RuntimeError(f"{nome} deve ser um número inteiro (recebido: {bruto!r}).") from None
    if valor < minimo:
        raise RuntimeError(f"{nome} deve ser >= {minimo} (recebido: {valor}).")
    return valor


@dataclass(frozen=True)
class Settings:
    ambiente: str
    secret_key: str

    # Expiracao
    access_ttl: timedelta          # vida do access token
    refresh_ttl: timedelta         # inatividade maxima
    sessao_max: timedelta          # tempo maximo de sessao
    refresh_reuse_grace: timedelta  # maximo de requisicoes paralelas com o mesmo refresh

    # Cookies 
    cookie_secure: bool
    cookie_samesite: str
    cookie_domain: str | None
    cookie_path: str = "/coordenacao"
    cookie_access: str = "sigcecp_access"
    cookie_refresh: str = "sigcecp_refresh"

    # Login
    login_max_tentativas: int = 5
    login_bloqueio: timedelta = timedelta(minutes=15)
    bcrypt_rounds: int = 12

    # CSRF 
    origens_confiaveis: frozenset[str] = frozenset()

    # JWT 
    jwt_algoritmo: str = "HS256"
    jwt_emissor: str = "sigcecp"
    jwt_audiencia: str = "sigcecp-admin"

    @property
    def jwt_key(self) -> bytes:
        return hmac.new(self.secret_key.encode(), b"sigcecp/jwt/v1", hashlib.sha256).digest()

    @property
    def csrf_key(self) -> bytes:
        return hmac.new(self.secret_key.encode(), b"sigcecp/csrf/v1", hashlib.sha256).digest()

    @classmethod
    def from_env(cls) -> "Settings":
        ambiente = os.getenv("APP_ENV", "development").strip().lower()
        if ambiente not in AMBIENTES:
            raise RuntimeError(f"APP_ENV deve ser um de {sorted(AMBIENTES)} (recebido: {ambiente!r}).")
        producao = ambiente == "production"

        segredo = os.getenv("AUTH_SECRET_KEY", "").strip()
        if segredo and len(segredo) < TAMANHO_MINIMO_SEGREDO:
            raise RuntimeError(
                f"AUTH_SECRET_KEY muito curta: use pelo menos {TAMANHO_MINIMO_SEGREDO} caracteres. "
                "Gere uma com: python -c \"import secrets; print(secrets.token_urlsafe(48))\""
            )
        if not segredo:
            if producao:
                raise RuntimeError("AUTH_SECRET_KEY é obrigatória em produção (APP_ENV=production).")
            segredo = secrets.token_urlsafe(48)
            logger.warning(
                "AUTH_SECRET_KEY não definida: usando uma chave efêmera. As sessões do "
                "administrador serão invalidadas a cada reinício. Defina a variável no .env."
            )

        cookie_secure = _ler_bool("COOKIE_SECURE", producao)
        if producao and not cookie_secure:
            raise RuntimeError("COOKIE_SECURE não pode ser false em produção.")
        samesite = os.getenv("COOKIE_SAMESITE", "strict").strip().lower()
        if samesite not in SAMESITE_VALIDOS:
            raise RuntimeError(f"COOKIE_SAMESITE deve ser um de {sorted(SAMESITE_VALIDOS)}.")
        if samesite == "none" and not cookie_secure:
            raise RuntimeError("COOKIE_SAMESITE=none exige COOKIE_SECURE=true.")

        origens = frozenset(
            o.strip().rstrip("/").lower()
            for o in os.getenv("TRUSTED_ORIGINS", "").split(",")
            if o.strip()
        )

        return cls(
            ambiente=ambiente,
            secret_key=segredo,
            access_ttl=timedelta(minutes=_ler_int("ACCESS_TOKEN_TTL_MINUTES", 15)),
            refresh_ttl=timedelta(days=_ler_int("REFRESH_TOKEN_TTL_DAYS", 7)),
            sessao_max=timedelta(days=_ler_int("SESSION_MAX_DAYS", 30)),
            refresh_reuse_grace=timedelta(seconds=_ler_int("REFRESH_REUSE_GRACE_SECONDS", 10, minimo=0)),
            cookie_secure=cookie_secure,
            cookie_samesite=samesite,
            cookie_domain=os.getenv("COOKIE_DOMAIN", "").strip() or None,
            login_max_tentativas=_ler_int("LOGIN_MAX_ATTEMPTS", 5),
            login_bloqueio=timedelta(minutes=_ler_int("LOGIN_LOCKOUT_MINUTES", 15)),
            bcrypt_rounds=_ler_int("BCRYPT_ROUNDS", 12, minimo=10),
            origens_confiaveis=origens,
        )

settings = Settings.from_env()