
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.eventos.models import Evento
from backend.eventos.schemas import EventoCreate


logger = logging.getLogger(__name__)

FUSO_BRASILIA = ZoneInfo("America/Sao_Paulo")
ESTADO_CLASSE = {
    "Em breve": "breve",
    "Em andamento": "andamento",
    "Encerrado": "encerrado",
}

def calcular_estado(evento: Evento, agora: datetime) -> str:
    if agora.tzinfo is None or agora.utcoffset() is None:
        raise ValueError("O instante atual deve incluir o fuso horário.")

    instante_local = agora.astimezone(FUSO_BRASILIA)
    inicio = datetime.combine(
        evento.data, evento.inicio, tzinfo=FUSO_BRASILIA
    )
    termino = datetime.combine(
        evento.data, evento.termino, tzinfo=FUSO_BRASILIA
    )

    if instante_local < inicio:
        return "Em breve"
    if instante_local <= termino:
        return "Em andamento"
    return "Encerrado"


def criar_evento(db: Session, dados: EventoCreate) -> Evento:
    """Cria um novo evento."""
    try:
        evento = Evento(**dados.model_dump())
        db.add(evento)
        db.commit()
        db.refresh(evento)
        return evento
    except Exception:
        db.rollback()
        raise


def listar_eventos(db: Session) -> list[Evento]:
    consulta = select(Evento).order_by(
        Evento.data, Evento.inicio, Evento.id
    )
    return list(db.scalars(consulta).all())


def buscar_evento_por_id(db: Session, evento_id: int) -> Evento | None:
    return db.get(Evento, evento_id)


def buscar_evento(db: Session, evento_id: int) -> Evento:
    """Busca um evento ou retorna erro 404."""
    evento = db.get(Evento, evento_id)

    if evento is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Evento não encontrado",
        )

    return evento


def atualizar_evento(
    db: Session,
    evento_id: int,
    dados: EventoCreate,
) -> Evento:
    """RF18: atualiza os dados de um evento existente."""
    evento = buscar_evento(db, evento_id)

    colunas = set(Evento.__table__.columns.keys()) - {"id"}

    try:
        for campo, valor in dados.model_dump().items():
            if campo in colunas:
                setattr(evento, campo, valor)

        db.commit()
        db.refresh(evento)

    except Exception:
        db.rollback()
        raise

    logger.info("Evento %s editado", evento_id)
    return evento


def remover_evento(db: Session, evento_id: int) -> None:
    """RF19: remove um evento existente."""
    evento = buscar_evento(db, evento_id)

    try:
        db.delete(evento)
        db.commit()

    except Exception:
        db.rollback()
        raise

    logger.info("Evento %s removido", evento_id)


