from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy import or_, select
from sqlalchemy.orm import Session
from typing import Annotated

from backend.auth import security
from backend.auth.dependencies import PROTECAO_ROOT
from backend.auth.models import Administrador
from backend.auth.services import PERFIL_COORDENADOR, USUARIO_MAX, criar_administrador, normalizar_usuario
from backend.config import templates
from backend.database import get_db

# Gestão de contas exclusiva do Root (protótipo aprovado em 10/11/2026)
router = APIRouter(
    prefix="/coordenacao/coordenadores",
    tags=["Coordenadores"],
    dependencies=PROTECAO_ROOT,
)


def _buscar_coordenador(db: Session, coordenador_id: int) -> Administrador | None:
    conta = db.get(Administrador, coordenador_id)
    return conta if conta is not None and conta.perfil == PERFIL_COORDENADOR else None


@router.get("", name="lista_coordenador")
def lista_coordenadores(request: Request, busca: str = "", situacao: str = "todos", db: Session = Depends(get_db)):
    consulta = select(Administrador).where(Administrador.perfil == PERFIL_COORDENADOR).order_by(Administrador.nome)
    if busca.strip():
        termo = f"%{busca.strip()}%"
        consulta = consulta.where(or_(Administrador.nome.ilike(termo), Administrador.usuario.ilike(termo)))
    if situacao == "ativos":
        consulta = consulta.where(Administrador.ativo.is_(True))
    elif situacao == "inativos":
        consulta = consulta.where(Administrador.ativo.is_(False))
    else:
        situacao = "todos"
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/coordenadores/lista-coordenador.html",
        context={"coordenadores": list(db.scalars(consulta)), "busca": busca.strip(), "situacao": situacao},
    )


@router.get("/novo", name="criar_coordenador")
def criar_coordenador_pagina(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/coordenadores/criar-coordenador.html",
        context={"valores": {}, "erros": {}},
    )


@router.post("/novo", name="salvar_coordenador")
def salvar_coordenador(
    request: Request,
    nome: Annotated[str, Form()] = "",
    usuario: Annotated[str, Form()] = "",
    senha: Annotated[str, Form()] = "",
    confirmar_senha: Annotated[str, Form()] = "",
    db: Session = Depends(get_db),
):
    nome = nome.strip()
    usuario_normalizado = normalizar_usuario(usuario)
    erros = {}

    if not nome:
        erros["nome"] = "Campo obrigatório. Informe o nome do coordenador."
    if not usuario_normalizado:
        erros["usuario"] = "Campo obrigatório. Informe o usuário de acesso."
    elif not 3 <= len(usuario_normalizado) <= USUARIO_MAX:
        erros["usuario"] = f"O usuário deve ter entre 3 e {USUARIO_MAX} caracteres."
    elif db.execute(select(Administrador.id).where(Administrador.usuario == usuario_normalizado)).first():
        erros["usuario"] = "Usuário já cadastrado. Escolha outro."

    if not senha:
        erros["senha"] = "Campo obrigatório. Defina a senha inicial."
    else:
        try:
            security.validar_politica_senha(senha, usuario_normalizado)
        except security.SenhaInvalida as erro:
            erros["senha"] = str(erro)
    if senha and senha != confirmar_senha:
        erros["confirmar_senha"] = "As senhas não coincidem. Digite a mesma senha inicial."

    if erros:
        # A senha nunca volta para o formulário
        return templates.TemplateResponse(
            request=request,
            name="coordenacao/coordenadores/criar-coordenador.html",
            context={"valores": {"nome": nome, "usuario": usuario.strip()}, "erros": erros},
            status_code=422,
        )

    conta = criar_administrador(db, usuario_normalizado, senha, nome_completo=nome, perfil=PERFIL_COORDENADOR)
    return RedirectResponse(request.url_for("coordenador_criado", coordenador_id=conta.id), status_code=303)


@router.get("/{coordenador_id}/criado", name="coordenador_criado")
def coordenador_criado(coordenador_id: int, request: Request, db: Session = Depends(get_db)):
    conta = _buscar_coordenador(db, coordenador_id)
    if conta is None:
        return RedirectResponse(request.url_for("lista_coordenador"), status_code=303)
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/coordenadores/coordenador-criado.html",
        context={"conta": conta},
    )
