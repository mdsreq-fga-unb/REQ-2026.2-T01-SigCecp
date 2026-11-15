from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.auth.dependencies import PROTECAO_ADMIN
from backend.config import templates
from backend.database import get_db
from backend.turmas.schemas import TurmaCreate
from backend.turmas.services import (
    atualizar_turma,
    buscar_turma,
    criar_turma,
    deletar_turma,
    listar_turmas,
    alunos_mock,
)

# Todas as rotas deste router são administrativas e exigem login.
router = APIRouter(
    prefix="/coordenacao/turmas",
    tags=["Turmas"],
    dependencies=PROTECAO_ADMIN,
)


@router.get("", name="lista_turma")
def lista_turmas_pagina(request: Request, db: Session = Depends(get_db)):
    turmas = listar_turmas(db)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/turmas/lista-turma.html",
        context={"turmas": turmas},
    )


# ============================================================
# CADASTRAR TURMA
# ============================================================

@router.get("/novo", name="cadastrar_turma")
def cadastrar_turma(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/turmas/cadastrar-turma.html",
        context={},
    )


@router.post("/novo", name="salvar_turma")
def salvar_turma(
    request: Request,
    dados: Annotated[TurmaCreate, Form()],
    db: Session = Depends(get_db),
):
    criar_turma(db, dados)

    return RedirectResponse(
        request.url_for("lista_turma"),
        status_code=303,
    )


# ============================================================
# EDITAR TURMA
# ============================================================

@router.get("/{turma_id}/editar", name="editar_turma")
def editar_turma(
    turma_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    turma = buscar_turma(db, turma_id)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/turmas/editar-turma.html",
        context={"turma": turma},
    )


@router.post("/{turma_id}/editar", name="salvar_edicao_turma")
def salvar_edicao_turma(
    turma_id: int,
    request: Request,
    dados: Annotated[TurmaCreate, Form()],
    db: Session = Depends(get_db),
):
    atualizar_turma(db, turma_id, dados)

    return RedirectResponse(
        request.url_for("lista_turma"),
        status_code=303,
    )


# ============================================================
# REMOVER TURMA
# ============================================================

@router.get("/{turma_id}/remover", name="confirmar_remocao_turma")
def confirmar_remocao_turma(
    turma_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    """Exibe a confirmação. Não remove a turma neste GET."""
    turma = buscar_turma(db, turma_id)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/turmas/remover-turma.html",
        context={"turma": turma},
    )


@router.post("/{turma_id}/remover", name="salvar_remocao_turma")
def salvar_remocao_turma(
    turma_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    deletar_turma(db, turma_id)

    return RedirectResponse(
        request.url_for("lista_turma"),
        status_code=303,
    )
    
#------------------------------------
# Ver Alunos Associados
#------------------------------------

@router.get("/{turma_id}/alunos", name="ver_alunos_associados")
def ver_alunos_associados(
    turma_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    turma = buscar_turma(db, turma_id)
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/turmas/ver-alunos.html",
        context={"turma": turma, "alunos": alunos_mock},
    )

@router.post("/{turma_id}/alunos")
def salvar_alunos_associados(
    turma_id: int,
    request: Request,
    dados: Annotated[TurmaCreate, Form()],
    db: Session = Depends(get_db),
):
    atualizar_turma(db, turma_id, dados)
    return RedirectResponse(
        request.url_for("ver_alunos_associados", turma_id=turma_id),
        status_code=303,
    )