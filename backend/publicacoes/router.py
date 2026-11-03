
from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    File,
    Form,
    Request,
    UploadFile,
)
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.config import templates

from backend.publicacoes.models import Publicacao
from backend.publicacoes.schemas import PublicacaoCreate

from backend.publicacoes.services import (
    atualizar_conteudo,
    buscar_conteudo,
    criar_conteudo_com_midias,
    remover_conteudo,
)


router = APIRouter(
    prefix="/coordenacao/conteudo",
    tags=["Publicações"],
)


@router.get("", name="lista_conteudo")
async def lista_conteudo(
    request: Request,
    db: Session = Depends(get_db),
):
    publicacoes = (
        db.query(Publicacao)
        .order_by(Publicacao.id.desc())
        .all()
    )

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/lista-conteudo.html",
        context={"publicacoes": publicacoes},
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
    titulo: Annotated[str, Form(...)],
    texto: Annotated[str, Form()] = "",
    imagem: Annotated[list[UploadFile] | None, File()] = None,
    video: Annotated[UploadFile | None, File()] = None,
    db: Session = Depends(get_db),
):

    dados = PublicacaoCreate(
        titulo=titulo,
        texto=texto or None,
    )

    criar_conteudo_com_midias(
        db=db,
        dados=dados,
        imagens=imagem,
        video=video,
    )

    return RedirectResponse(
        url=str(request.url_for("lista_conteudo")),
        status_code=303,
    )


@router.get("/{conteudo_id}/editar", name="editar_conteudo")
def editar_conteudo_form(
    conteudo_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    conteudo = buscar_conteudo(db, conteudo_id)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/editar-conteudo.html",
        context={"conteudo": conteudo},
    )


@router.post(
    "/{conteudo_id}/editar",
    name="salvar_edicao_conteudo",
)
def salvar_edicao_conteudo(
    conteudo_id: int,
    request: Request,
    dados: Annotated[PublicacaoCreate, Form()],
    db: Session = Depends(get_db),
):
    atualizar_conteudo(db, conteudo_id, dados)

    return RedirectResponse(
        request.url_for("modulo_conteudo_publico"),
        status_code=303,
    )


@router.get(
    "/{conteudo_id}/remover",
    name="confirmar_remocao_conteudo",
)
def confirmar_remocao_conteudo(
    conteudo_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    conteudo = buscar_conteudo(db, conteudo_id)

    return templates.TemplateResponse(
        request=request,
        name="coordenacao/conteudo/remover-conteudo.html",
        context={"conteudo": conteudo},
    )


@router.post(
    "/{conteudo_id}/remover",
    name="excluir_conteudo",
)
def excluir_conteudo(
    conteudo_id: int,
    request: Request,
    db: Session = Depends(get_db),
):
    remover_conteudo(db, conteudo_id)

    return RedirectResponse(
        request.url_for("modulo_conteudo_publico"),
        status_code=303,
    )
