"""Middleware da área administrativa (/coordenacao/*)"""

import logging

from starlette.concurrency import run_in_threadpool
from starlette.datastructures import MutableHeaders
from starlette.requests import cookie_parser

from backend import database
from backend.auth import cookies, security
from backend.auth import settings as cfg
from backend.auth import services

logger = logging.getLogger("sigcecp.auth")

PREFIXO_ADMIN = "/coordenacao"
PREFIXO_AUTH = "/coordenacao/auth/"

def _area_admin(caminho: str) -> bool:
    return caminho == PREFIXO_ADMIN or caminho.startswith(PREFIXO_ADMIN + "/")


def _renovar_em_thread(refresh_token: str) -> services.SessaoEmitida:
    db = database.SessionLocal()
    try:
        return services.renovar_sessao(db, refresh_token)
    finally:
        db.close()


def _cookies_da_requisicao(scope) -> dict[str, str]:
    brutos = b"; ".join(v for k, v in scope["headers"] if k == b"cookie")
    return cookie_parser(brutos.decode("latin-1")) if brutos else {}


def _reescrever_cookies(scope, alteracoes: dict[str, str | None]) -> None:
    """Troca (ou remove, se valor None) cookies nos cabeçalhos da requisição em andamento."""
    atuais = _cookies_da_requisicao(scope)
    for nome, valor in alteracoes.items():
        if valor is None:
            atuais.pop(nome, None)
        else:
            atuais[nome] = valor
    cabecalhos = [(k, v) for k, v in scope["headers"] if k != b"cookie"]
    if atuais:
        cabecalhos.append((b"cookie", "; ".join(f"{k}={v}" for k, v in atuais.items()).encode("latin-1")))
    scope["headers"] = cabecalhos


class SessaoAdminMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] != "http" or not _area_admin(scope["path"]):
            await self.app(scope, receive, send)
            return

        set_cookies: list[str] = []
        if not scope["path"].startswith(PREFIXO_AUTH):
            set_cookies = await self._renovar_se_necessario(scope)

        async def enviar(mensagem):
            if mensagem["type"] == "http.response.start":
                cabecalhos = MutableHeaders(scope=mensagem)
                cabecalhos.setdefault("Cache-Control", "no-store")
                cabecalhos.setdefault("X-Frame-Options", "DENY")
                for valor in set_cookies:
                    cabecalhos.append("Set-Cookie", valor)
            await send(mensagem)

        await self.app(scope, receive, enviar)

    async def _renovar_se_necessario(self, scope) -> list[str]:
        s = cfg.settings
        presentes = _cookies_da_requisicao(scope)
        access, refresh = presentes.get(s.cookie_access), presentes.get(s.cookie_refresh)

        if access and security.decodificar_access_token(access) is not None:
            return []
        if not refresh:
            return [] 

        try:
            sessao = await run_in_threadpool(_renovar_em_thread, refresh)
        except services.RefreshInvalido as erro:
            logger.info("Renovação recusada: %s", erro.motivo)
            if not erro.limpar_cookies:
                return []
            _reescrever_cookies(scope, {s.cookie_access: None, s.cookie_refresh: None})
            return cookies.cabecalhos_set_cookie(cookies.limpar_cookies)
        except Exception:
            logger.exception("Erro ao renovar a sessão do administrador")
            _reescrever_cookies(scope, {s.cookie_access: None})
            return []

        _reescrever_cookies(scope, {s.cookie_access: sessao.access_token, s.cookie_refresh: sessao.refresh_token})
        return cookies.cabecalhos_set_cookie(lambda r: cookies.definir_cookies(r, sessao))
