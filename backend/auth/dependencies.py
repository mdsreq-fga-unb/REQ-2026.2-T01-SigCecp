"""Dependências do FastAPI para proteger a área administrativa

Uso nas rotas administrativas

    router = APIRouter(prefix="/coordenacao/...", dependencies=PROTECAO_ADMIN)
"""

from fastapi import Depends, HTTPException, Request, status
from sqlalchemy.orm import Session

from backend.auth import settings as cfg
from backend.auth.csrf import verificar_csrf
from backend.auth.errors import nao_autenticado
from backend.auth.models import Administrador
from backend.auth.security import decodificar_access_token
from backend.auth.services import PERFIL_ROOT, validar_sessao
from backend.database import get_db


def exigir_admin(request: Request, db: Session = Depends(get_db)) -> Administrador:

    token = request.cookies.get(cfg.settings.cookie_access)
    if not token:
        raise nao_autenticado()

    claims = decodificar_access_token(token)
    if claims is None:
        raise nao_autenticado()

    admin = validar_sessao(db, int(claims["sub"]), claims["sid"])
    if admin is None:
        raise nao_autenticado()

    request.state.admin = admin
    request.state.admin_sid = claims["sid"]
    return admin


def exigir_root(admin: Administrador = Depends(exigir_admin)) -> Administrador:
    """Só o Root gerencia as contas de coordenador."""
    if admin.perfil != PERFIL_ROOT:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Área exclusiva do Root.")
    return admin


PROTECAO_ADMIN = [Depends(exigir_admin), Depends(verificar_csrf)]
PROTECAO_ROOT = [Depends(exigir_root), Depends(verificar_csrf)]
