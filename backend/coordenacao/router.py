from fastapi import APIRouter, Request

from backend.auth.dependencies import PROTECAO_ADMIN
from backend.config import templates

# Página inicial da área administrativa, com as ações de cada área (protótipo de 10/11/2026)
router = APIRouter(
    prefix="/coordenacao",
    tags=["Coordenação"],
    dependencies=PROTECAO_ADMIN,
)


@router.get("", name="inicio_coordenacao")
def inicio_coordenacao(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/inicio.html",
        context={},
    )
