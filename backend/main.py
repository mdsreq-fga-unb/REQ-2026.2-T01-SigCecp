
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from backend.config import ASSETS_DIR, templates
from backend.publicacoes.router import router as publicacoes_router


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
async def modulo_eventos_publico(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="publico/modulo-eventos.html",
        context={},
    )


app.include_router(publicacoes_router)
