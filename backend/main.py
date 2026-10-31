
from datetime import datetime

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session

from backend.config import ASSETS_DIR, templates
from backend.database import get_db
from backend.eventos.services import (
    FUSO_BRASILIA,
    buscar_evento_por_id,
    calcular_estado,
    listar_eventos,
)
from backend.publicacoes.router import router as publicacoes_router

from backend.eventos.router import router as eventos_router
   



app = FastAPI(
    title="SigCECP",
)

# Arquivos estáticos: CSS, JavaScript e imagens.
app.mount(
    "/static",
    StaticFiles(directory=ASSETS_DIR),
    name="static",
)


@app.get("/", name="modulo_conteudo_publico")
async def modulo_conteudo_publico(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="publico/modulo-conteudo.html",
        context={},
    )


@app.get("/eventos", name="modulo_eventos_publico")
def modulo_eventos_publico(request: Request, db: Session = Depends(get_db)):
    agora = datetime.now(FUSO_BRASILIA)
    eventos = [
        (evento, calcular_estado(evento, agora))
        for evento in listar_eventos(db)
    ]
    return templates.TemplateResponse(
        request=request,
        name="publico/modulo-eventos.html",
        context={"eventos": eventos},
    )


@app.get("/eventos/{evento_id}", name="detalhe_evento_publico")
def detalhe_evento_publico(
    request: Request, evento_id: int, db: Session = Depends(get_db),
):
    evento = buscar_evento_por_id(db, evento_id)
    if evento is None:
        raise HTTPException(status_code=404, detail="Evento não encontrado.")

    return templates.TemplateResponse(
        request=request,
        name="publico/detalhe-evento.html",
        context={
            "evento": evento,
            "estado": calcular_estado(evento, datetime.now(FUSO_BRASILIA)),
        },
    )


app.include_router(publicacoes_router)
app.include_router(eventos_router)