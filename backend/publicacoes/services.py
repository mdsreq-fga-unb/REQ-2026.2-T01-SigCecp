import logging
from datetime import datetime
from zoneinfo import ZoneInfo
 
from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session
 
from backend.publicacoes.models import Publicacao
from backend.publicacoes.schemas import PublicacaoCreate
 
 
logger = logging.getLogger(__name__)
 
def criar_conteudo(db: Session, dados: PublicacaoCreate) -> Publicacao:
    
    try:
        publicacao = Publicacao(**dados.model_dump())
        db.add(publicacao)
        db.commit()
        db.refresh(publicacao)
        return publicacao
    except Exception:
        db.rollback()
        raise