"""Exceção da área administrativa"""

from fastapi import HTTPException


class ErroAcessoAdmin(HTTPException):
    """401 (sem sessão válida) ou 403 (CSRF/origem rejeitados) na área administrativa"""


def nao_autenticado(detalhe: str = "Autenticação necessária.") -> ErroAcessoAdmin:
    return ErroAcessoAdmin(status_code=401, detail=detalhe)


def acesso_negado(detalhe: str = "Requisição não autorizada.") -> ErroAcessoAdmin:
    return ErroAcessoAdmin(status_code=403, detail=detalhe)
