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

def listar_conteudos(db: Session) -> list[Publicacao]:
    consulta = select(Publicacao).order_by(Publicacao.id)
    return list(db.scalars(consulta).all())


def buscar_conteudo_por_id(db: Session, conteudo_id: int) -> Publicacao | None:
    return db.get(Publicacao, conteudo_id)


def buscar_conteudo(db: Session, conteudo_id: int) -> Publicacao:
    conteudo = db.get(Publicacao, conteudo_id)

    if conteudo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Publicação não encontrada",
        )

    return conteudo


def atualizar_conteudo(
    db: Session,
    conteudo_id: int,
    dados: PublicacaoCreate,
) -> Publicacao:
    conteudo = buscar_conteudo(db, conteudo_id)

    colunas = set(Publicacao.__table__.columns.keys()) - {"id"}

    try:
        for campo, valor in dados.model_dump().items():
            if campo in colunas:
                setattr(conteudo, campo, valor)

        db.commit()
        db.refresh(conteudo)

    except Exception:
        db.rollback()
        raise

    logger.info("Publicação %s editada", conteudo_id)
    return conteudo


def remover_conteudo(db: Session, conteudo_id: int) -> None:
    conteudo = buscar_conteudo(db, conteudo_id)

    try:
        db.delete(conteudo)
        db.commit()

    except Exception:
        db.rollback()
        raise

    logger.info("Publicação %s removida", conteudo_id)