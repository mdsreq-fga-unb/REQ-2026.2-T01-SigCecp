
from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.config import templates
from backend.database import get_db
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import (
    atualizar_evento,
    buscar_evento,
    criar_evento,
    remover_evento,
)

router = APIRouter(tags=["Eventos"])


# ============================================================
# PUBLICAR EVENTO
# ============================================================

@router.get("/coordenacao/eventos/novo", name="publicar_evento")
def publicar_evento(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/eventos/publicar-evento.html",
        context={},
    )


@router.post("/coordenacao/eventos/novo", name="salvar_evento")
def salvar_evento(
    request: Request,
    dados: Annotated[EventoCreate, Form()],
    db: Session = Depends(get_db),
):
    criar_evento(db, dados)

    return RedirectResponse(
        request.url_for("modulo_eventos_publico"),
        status_code=303,
    )


# ============================================================
# EDITAR EVENTO
# ============================================================

@router.get(
    "/coordenacao/eventos/{evento_id}/editar",
    name="editar_evento",
)
def editar_evento_form(
    evento_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    evento = buscar_evento(db, evento_id)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/eventos/editar-evento.html",
        context={"evento": evento},
    )


@router.post(
    "/coordenacao/eventos/{evento_id}/editar",
    name="salvar_edicao_evento",
)
def salvar_edicao_evento(
    evento_id: int,
    request: Request,
    dados: Annotated[EventoCreate, Form()],
    db: Session = Depends(get_db),
):
    atualizar_evento(db, evento_id, dados)

    return RedirectResponse(
        request.url_for("modulo_eventos_publico"),
        status_code=303,
    )


# ============================================================
# REMOVER EVENTO
# ============================================================

@router.get(
    "/coordenacao/eventos/{evento_id}/remover",
    name="confirmar_remocao_evento",
)
def confirmar_remocao_evento(
    evento_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    """Exibe a confirmação. Não remove o evento neste GET."""

    evento = buscar_evento(db, evento_id)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/eventos/remover-evento.html",
        context={"evento": evento},
    )


@router.post(
    "/coordenacao/eventos/{evento_id}/remover",
    name="excluir_evento",
)
def excluir_evento(
    evento_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    remover_evento(db, evento_id)

    return RedirectResponse(
        request.url_for("modulo_eventos_publico"),
        status_code=303,
    )
