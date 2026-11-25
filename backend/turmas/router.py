from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.alunos.services import (
    alunos_da_turma,
    alunos_para_associar,
    associar_aluno_turma,
    contar_alunos_por_turma,
)
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
        context={"turmas": turmas, "alunos_por_turma": contar_alunos_por_turma(db)},
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
        context={"turma": turma, "alunos": alunos_da_turma(db, turma_id)},
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
        context={"turma": turma, "alunos": alunos_da_turma(db, turma_id), "aviso": request.query_params.get("aviso")},
    )

#---------------------------
# Associar Alunos (RF06)
#---------------------------
def _tela_associar(request: Request, db: Session, turma_id: int, erro: str | None = None, status_code: int = 200):
    turma = buscar_turma(db, turma_id)
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/turmas/associar-alunos.html",
        context={
            "turma": turma,
            "turmas": listar_turmas(db),
            "alunos": alunos_para_associar(db, turma_id),
            "aluno_escolhido": request.query_params.get("aluno"),
            "erro": erro,
        },
        status_code=status_code,
    )


@router.get("/{turma_id}/alunos/associar", name="associar_alunos")
def associar_alunos(
    turma_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    return _tela_associar(request, db, turma_id)


@router.post("/{turma_id}/alunos", name="salvar_alunos_associados")
def salvar_alunos_associados(
    turma_id: int,
    request: Request,
    aluno_id: Annotated[str, Form()] = "",
    db: Session = Depends(get_db),
):
    buscar_turma(db, turma_id)
    if not aluno_id.isdigit():
        return _tela_associar(request, db, turma_id, "Selecione o aluno que será associado à turma.", 422)

    admin = getattr(request.state, "admin", None)
    associar_aluno_turma(db, turma_id, int(aluno_id), getattr(admin, "usuario", "coordenação"))
    return RedirectResponse(
        str(request.url_for("ver_alunos_associados", turma_id=turma_id)) + "?aviso=associado",
        status_code=303,
    )
