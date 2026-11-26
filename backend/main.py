
from datetime import datetime
from pathlib import Path

from fastapi import Depends, FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
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
from backend.erros import tratar_http, tratar_validacao
from backend.auth.middleware import SessaoAdminMiddleware
from backend.auth.router import router as auth_router, tratar_erro_acesso
from backend.turmas.router import router as turmas_router
from backend.alunos.router import router as alunos_router
from backend.coordenadores.router import router as coordenadores_router
from backend.coordenacao.router import router as coordenacao_router
from backend.eventos.router import router as eventos_router
   

app = FastAPI(
    title="SigCECP",
)

# Autenticação do administrador (/coordenacao)
app.add_middleware(SessaoAdminMiddleware)
app.add_exception_handler(ErroAcessoAdmin, tratar_erro_acesso)
# Erros como página em português para o navegador (acessibilidade: WCAG 3.3.1 e 3.3.3)
app.add_exception_handler(RequestValidationError, tratar_validacao)
app.add_exception_handler(StarletteHTTPException, tratar_http)

BASE_DIR = Path(__file__).resolve().parent.parent
MEDIA_DIR = BASE_DIR / "backend" / "media"
class ArquivosEstaticos(StaticFiles):
    """Pede ao navegador que confira se o CSS e o JavaScript mudaram antes de usar a cópia guardada.

    Sem isso, depois de uma atualização o navegador pode continuar usando o CSS antigo.
    Quando o arquivo não mudou, a resposta é um 304, sem baixar de novo.
    """

    async def get_response(self, path, scope):
        resposta = await super().get_response(path, scope)
        resposta.headers["Cache-Control"] = "no-cache"
        return resposta


# Arquivos estáticos: CSS, JavaScript e imagens.
app.mount(
    "/static",
    ArquivosEstaticos(directory=ASSETS_DIR),
    name="static",
)

# Arquivos enviados pelos usuários.
app.mount(
    "/media",
    StaticFiles(directory=MEDIA_DIR),
    name="media",
)

@app.get("/", name="modulo_conteudo_publico")
def modulo_conteudo_publico(request: Request, db: Session = Depends(get_db)):
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
    # Próximos e em andamento primeiro, do mais perto ao mais distante; encerrados à parte, do mais recente
    proximos = [item for item in eventos if item[1] != "Encerrado"]
    encerrados = [item for item in reversed(eventos) if item[1] == "Encerrado"]
    return templates.TemplateResponse(
        request=request,
        name="publico/modulo-eventos.html",
        context={"eventos": eventos, "proximos": proximos, "encerrados": encerrados},
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
app.include_router(turmas_router)
app.include_router(alunos_router)
app.include_router(coordenadores_router)
app.include_router(coordenacao_router)