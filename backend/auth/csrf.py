"""Proteção contra CSRF"""

import hashlib
import hmac
import secrets
from urllib.parse import urlsplit

from fastapi import Request
from markupsafe import Markup

from backend.auth import settings as cfg
from backend.auth.errors import acesso_negado, nao_autenticado

METODOS_SEGUROS = frozenset({"GET", "HEAD", "OPTIONS", "TRACE"})
CAMPO_FORM = "csrf_token"
CABECALHO = "x-csrf-token"
_TIPOS_FORM = ("application/x-www-form-urlencoded", "multipart/form-data")
_TAMANHO_MAX_TOKEN = 128

MENSAGEM_CSRF = (
    "Não foi possível validar a segurança da requisição. "
    "Volte, recarregue a página e tente novamente."
)


def _mac(sid: str, nonce: str) -> str:
    return hmac.new(cfg.settings.csrf_key, f"{sid}.{nonce}".encode(), hashlib.sha256).hexdigest()


def gerar_token(sid: str) -> str:
    nonce = secrets.token_hex(16)
    return f"{nonce}.{_mac(sid, nonce)}"


def validar_token(token: str, sid: str) -> bool:
    if not token or len(token) > _TAMANHO_MAX_TOKEN or not sid:
        return False
    nonce, separador, mac = token.partition(".")
    if not separador or not nonce:
        return False
    return hmac.compare_digest(_mac(sid, nonce), mac)


def verificar_origem(request: Request) -> None:
    if request.method in METODOS_SEGUROS:
        return
    origem = request.headers.get("origin")
    if origem is None:
        referer = request.headers.get("referer")
        if not referer:
            return
        partes = urlsplit(referer)
        origem = f"{partes.scheme}://{partes.netloc}"

    if origem == "null":
        raise acesso_negado(MENSAGEM_CSRF)

    partes = urlsplit(origem)
    host = request.headers.get("host", "")
    if partes.netloc and partes.netloc.lower() == host.lower():
        return
    if origem.rstrip("/").lower() in cfg.settings.origens_confiaveis:
        return
    raise acesso_negado(MENSAGEM_CSRF)


async def verificar_csrf(request: Request) -> None:
    if request.method in METODOS_SEGUROS:
        return

    verificar_origem(request)

    sid = getattr(request.state, "admin_sid", None)
    if not sid:
        raise nao_autenticado()

    token = request.headers.get(CABECALHO)
    if token is None and request.headers.get("content-type", "").lower().startswith(_TIPOS_FORM):
        token = (await request.form()).get(CAMPO_FORM)

    if not isinstance(token, str) or not validar_token(token, sid):
        raise acesso_negado(MENSAGEM_CSRF)


def contexto_csrf(request: Request) -> dict:
    sid = getattr(request.state, "admin_sid", None)
    token = gerar_token(sid) if sid else ""
    campo = Markup(f'<input type="hidden" name="{CAMPO_FORM}" value="{token}">') if token else Markup("")
    return {"csrf_token": token, "csrf_input": campo}
