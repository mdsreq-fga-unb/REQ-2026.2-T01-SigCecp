"""Rotas de autenticação do administrador

    GET  /coordenacao/auth/login    página de login
    POST /coordenacao/auth/login    valida usuário/senha e abre a sessão
    POST /coordenacao/auth/refresh  renova explicitamente o access token
    POST /coordenacao/auth/logout   encerra a sessão

"""

from typing import Annotated

from fastapi import APIRouter, Depends, Form, Header, Request
from fastapi.responses import JSONResponse, RedirectResponse, Response
from sqlalchemy.orm import Session

from backend.auth import settings as cfg
from backend.auth.cookies import definir_cookies, limpar_cookies
from backend.auth.csrf import MENSAGEM_CSRF, validar_token, verificar_origem
from backend.auth.errors import ErroAcessoAdmin, acesso_negado, nao_autenticado
from backend.auth.schemas import LoginForm
from backend.auth.services import (
    USUARIO_MAX,
    CredenciaisInvalidas,
    RefreshInvalido,
    autenticar,
    encerrar_sessao,
    familia_do_refresh,
    iniciar_sessao,
    renovar_sessao,
)
from backend.config import templates
from backend.database import get_db

router = APIRouter(prefix="/coordenacao/auth", tags=["Autenticação"])

MENSAGEM_LOGIN_INVALIDO = (
    "Usuário ou senha inválidos, ou acesso temporariamente bloqueado após várias "
    "tentativas. Aguarde alguns minutos e tente novamente."
)


def _pagina_login(request: Request, status_code: int = 200, erro: str | None = None, usuario: str = ""):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/login.html",
        context={"erro": erro, "usuario": usuario},
        status_code=status_code,
    )


def _redirecionar(request: Request, rota: str) -> RedirectResponse:
    return RedirectResponse(request.app.url_path_for(rota), status_code=303)


def _exigir_csrf_da_sessao(familia: str, form_token: str | None, header_token: str | None) -> None:
    token = header_token or form_token
    if not token or not validar_token(token, familia):
        raise acesso_negado(MENSAGEM_CSRF)



@router.get("/login", name="login_pagina", include_in_schema=False)
def login_pagina(request: Request):
    return _pagina_login(request)


@router.post("/login", name="login")
def login(
    request: Request,
    dados: Annotated[LoginForm, Form()],
    db: Session = Depends(get_db),
):

    verificar_origem(request)

    try:
        admin = autenticar(db, dados.usuario, dados.senha)
    except CredenciaisInvalidas:
        return _pagina_login(request, 401, MENSAGEM_LOGIN_INVALIDO, dados.usuario[:USUARIO_MAX])

    anterior = request.cookies.get(cfg.settings.cookie_refresh)
    if anterior:
        familia = familia_do_refresh(db, anterior)
        if familia:
            encerrar_sessao(db, familia)

    sessao = iniciar_sessao(db, admin)
    resposta = _redirecionar(request, "lista_conteudo")
    definir_cookies(resposta, sessao)
    return resposta


@router.post("/refresh", name="refresh", status_code=204)
def refresh(
    request: Request,
    csrf_token: Annotated[str | None, Form()] = None,
    x_csrf_token: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db),
):
    verificar_origem(request)

    token = request.cookies.get(cfg.settings.cookie_refresh)
    if not token:
        raise nao_autenticado()
    familia = familia_do_refresh(db, token)
    if familia is None:
        resposta = JSONResponse({"detail": "Sessão inválida."}, status_code=401)
        limpar_cookies(resposta)
        return resposta
    _exigir_csrf_da_sessao(familia, csrf_token, x_csrf_token)

    try:
        sessao = renovar_sessao(db, token)
    except RefreshInvalido as erro:
        resposta = JSONResponse({"detail": "Sessão expirada. Faça login novamente."}, status_code=401)
        if erro.limpar_cookies:
            limpar_cookies(resposta)
        return resposta

    resposta = Response(status_code=204)
    definir_cookies(resposta, sessao)
    return resposta


@router.post("/logout", name="logout")
def logout(
    request: Request,
    csrf_token: Annotated[str | None, Form()] = None,
    x_csrf_token: Annotated[str | None, Header()] = None,
    db: Session = Depends(get_db),
):

    verificar_origem(request)

    token = request.cookies.get(cfg.settings.cookie_refresh)
    familia = familia_do_refresh(db, token) if token else None
    if familia:
        _exigir_csrf_da_sessao(familia, csrf_token, x_csrf_token)
        encerrar_sessao(db, familia)

    resposta = _redirecionar(request, "login_pagina")
    limpar_cookies(resposta)
    return resposta


async def tratar_erro_acesso(request: Request, exc: ErroAcessoAdmin):
    if "text/html" in request.headers.get("accept", ""):
        if exc.status_code == 401:
            titulo, mensagem = (
                "Acesso restrito",
                "É necessário entrar com o usuário da Coordenação para continuar.",
            )
        else:
            titulo, mensagem = "Requisição recusada", exc.detail
        return templates.TemplateResponse(
            request=request,
            name="coordenacao/restrito.html",
            context={"titulo": titulo, "mensagem": mensagem, "sem_login": exc.status_code == 401},
            status_code=exc.status_code,
        )
    return JSONResponse({"detail": exc.detail}, status_code=exc.status_code)
