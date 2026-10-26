
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from backend.config import ASSETS_DIR, templates
from backend.database import Base, engine
from backend.publicacoes import models as publicacoes_models
from backend.publicacoes.router import router as publicacoes_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Cria as tabelas que ainda não existem.
    Base.metadata.create_all(bind=engine)
    yield


app = FastAPI(
    title="SigCECP",
    lifespan=lifespan,
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
async def modulo_eventos_publico(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="publico/modulo-eventos.html",
        context={},
    )


app.include_router(publicacoes_router)
