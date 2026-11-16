from datetime import datetime
from typing import Annotated
from fastapi import APIRouter, Depends, Form, Request, UploadFile, File
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from backend.eventos.models import Evento
from backend.config import templates
from backend.database import get_db
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import (
    FUSO_BRASILIA,
    ESTADO_CLASSE,
    atualizar_evento,
    buscar_evento,
    criar_evento,
    remover_evento,
    calcular_estado
)


router = APIRouter(tags=["Eventos"], prefix="/coordenacao/eventos")


@router.get("", name="lista_evento")
async def lista_eventos_pagina(request: Request, db: Session = Depends(get_db)):
    agora = datetime.now(FUSO_BRASILIA)

    eventos = db.query(Evento).order_by(Evento.data.desc(), Evento.inicio.desc()).all()
    for evento in eventos:
        evento.estado = ESTADO_CLASSE[calcular_estado(evento, agora)]

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/eventos/lista-evento.html",
        context={"eventos": eventos, "agora": agora},
    )


# ============================================================
# PUBLICAR EVENTO
# ============================================================

@router.get("/novo", name="publicar_evento")
def publicar_evento(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/eventos/publicar-evento.html",
        context={},
    )


@router.post("/novo", name="salvar_evento")
def salvar_evento(
    request: Request,
    dados: Annotated[EventoCreate, Form()],
    imagem: Annotated[UploadFile | None, File()] = None,
    video: Annotated[UploadFile | None, File()] = None,
    db: Session = Depends(get_db),
):
    criar_evento(db, dados, imagem=imagem, video=video)

    return RedirectResponse(
        request.url_for("modulo_eventos_publico"),
        status_code=303,
    )

# ============================================================
# EDITAR EVENTO
# ============================================================

@router.get("/{evento_id}/editar", name="editar_evento")
def editar_evento(
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

@router.post("/{evento_id}/editar", name="salvar_edicao_evento")
def salvar_edicao_evento(
    evento_id: int,
    request: Request,
    dados: Annotated[EventoCreate, Form()],
    imagem: Annotated[UploadFile | None, File()] = None,
    video: Annotated[UploadFile | None, File()] = None,
    remover_imagem: Annotated[bool, Form()] = False,
    remover_video: Annotated[bool, Form()] = False,
    db: Session = Depends(get_db),
):
    atualizar_evento(
        db,
        evento_id,
        dados,
        imagem=imagem,
        video=video,
        remover_imagem=remover_imagem,
        remover_video=remover_video,
    )

    return RedirectResponse(
        request.url_for("modulo_eventos_publico"),
        status_code=303,
    )

# ============================================================
# REMOVER EVENTO
# ============================================================

@router.get("/{evento_id}/remover", name="confirmar_remocao_evento")
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

@router.post("/{evento_id}/remover", name="salvar_remocao_evento")
def salvar_remocao_evento(
    evento_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    remover_evento(db, evento_id)

    return RedirectResponse(
        request.url_for("lista_evento"),
        status_code=303,
    )