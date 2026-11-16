
from datetime import datetime
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from backend.publicacoes.models import Publicacao
from backend.config import ASSETS_DIR, templates
from backend.database import get_db
from backend.publicacoes.services import buscar_conteudo_por_id
from backend.eventos.services import (
    FUSO_BRASILIA,
    buscar_evento_por_id,
    calcular_estado,
    listar_eventos,
)
from backend.publicacoes.router import router as publicacoes_router
from backend.auth.errors import ErroAcessoAdmin
from backend.auth.middleware import SessaoAdminMiddleware
from backend.auth.router import router as auth_router, tratar_erro_acesso

from backend.eventos.router import router as eventos_router
   

app = FastAPI(
    title="SigCECP",
)

# Autenticação do administrador (/coordenacao)
app.add_middleware(SessaoAdminMiddleware)
app.add_exception_handler(ErroAcessoAdmin, tratar_erro_acesso)

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / "backend" / "media"
# Arquivos estáticos: CSS, JavaScript e imagens.
app.mount(
    "/static",
    StaticFiles(directory=ASSETS_DIR),
    name="static",
)

# Arquivos enviados pelos usuários.
app.mount(
    "/media",
    StaticFiles(directory=MEDIA_DIR),
    name="media",
)

@app.get("/", name="modulo_conteudo_publico")
async def modulo_conteudo_publico(request: Request, db: Session = Depends(get_db)):
    publicacoes = db.query(Publicacao).order_by(Publicacao.id.desc()).all()

    return templates.TemplateResponse(
        request=request,
        name="publico/modulo-conteudo.html",  
        context={"publicacoes": publicacoes},
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

@app.get("/conteudo/{conteudo_id}", name="detalhe_conteudo_publico")
def detalhe_conteudo_publico(
    request: Request, conteudo_id: int, db: Session = Depends(get_db),
):
    conteudo = buscar_conteudo_por_id(db, conteudo_id)
    if conteudo is None:
        raise HTTPException(status_code=404, detail="Publicação não encontrada.")

    return templates.TemplateResponse(
        request=request,
        name="publico/detalhe-conteudo.html",
        context={
            "conteudo": conteudo,
        },
    )

app.include_router(auth_router)
app.include_router(publicacoes_router)
app.include_router(eventos_router)