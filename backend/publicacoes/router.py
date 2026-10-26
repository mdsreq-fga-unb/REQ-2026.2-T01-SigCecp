from fastapi import APIRouter, Depends, Form, Request
from fastapi.responses import RedirectResponse, HTMLResponse
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.publicacoes.models import Publicacao
from backend.config import templates

router = APIRouter(
    prefix="/coordenacao/conteudo",
    tags=["Publicações"],
)


@router.get("", name="lista_conteudo", response_class=HTMLResponse)
async def listar_publicacoes(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/lista-conteudo.html",
        context={"publicacoes": []},
    )

@router.get("/novo", name="publicar_conteudo")
async def publicar_conteudo(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/publicar-conteudo.html",
        context={},
    )

@router.post("/novo", name="salvar_conteudo")
async def salvar_conteudo(
    request: Request,
    titulo: str = Form(...),
    texto: str = Form(...),
):
    print("Título:", titulo)
    print("Texto:", texto)

    return RedirectResponse(
        url=str(request.url_for("lista_conteudo")),
        status_code=303,
    )

router = APIRouter(
    prefix="/coordenacao/conteudo",
    tags=["Publicações"],
)


@router.get("", name="lista_conteudo")
async def lista_conteudo(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/lista-conteudo.html",
        context={},
    )


@router.get("/novo", name="publicar_conteudo")
async def exibir_formulario(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/publicar-conteudo.html",
        context={},
    )


@router.post("/novo", name="salvar_conteudo")
async def salvar_conteudo(
    request: Request,
    titulo: str = Form(...),
    texto: str = Form(""),
    db: Session = Depends(get_db),
):
    publicacao = Publicacao(
        titulo=titulo,
        texto=texto or None,
    )

    db.add(publicacao)
    db.commit()

    return RedirectResponse(
        url=str(request.url_for("lista_conteudo")),
        status_code=303,
    )