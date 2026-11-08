"""Emissão e remoção dos cookies de sessão"""

from starlette.responses import Response

from backend.auth import settings as cfg
from backend.auth.services import SessaoEmitida


def definir_cookies(response: Response, sessao: SessaoEmitida) -> None:
    s = cfg.settings
    comuns = dict(
        path=s.cookie_path,
        domain=s.cookie_domain,
        secure=s.cookie_secure,
        httponly=True,
        samesite=s.cookie_samesite,
    )
    response.set_cookie(s.cookie_access, sessao.access_token, max_age=sessao.access_max_age, **comuns)
    response.set_cookie(s.cookie_refresh, sessao.refresh_token, max_age=sessao.refresh_max_age, **comuns)


def limpar_cookies(response: Response) -> None:
    s = cfg.settings
    comuns = dict(
        path=s.cookie_path,
        domain=s.cookie_domain,
        secure=s.cookie_secure,
        httponly=True,
        samesite=s.cookie_samesite,
    )
    response.delete_cookie(s.cookie_access, **comuns)
    response.delete_cookie(s.cookie_refresh, **comuns)


def cabecalhos_set_cookie(preencher) -> list[str]:
    auxiliar = Response()
    preencher(auxiliar)
    return [v.decode("latin-1") for k, v in auxiliar.raw_headers if k == b"set-cookie"]
