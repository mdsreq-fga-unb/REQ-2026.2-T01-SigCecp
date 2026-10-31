from typing import Annotated

from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.config import templates
from backend.database import get_db
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import criar_evento

router = APIRouter(tags=["Eventos"])


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
        request.url_for("modulo_eventos_publico"), status_code=303,
    )