from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.eventos.models import Evento
from backend.eventos.schemas import EventoCreate


def criar_evento(db: Session, dados: EventoCreate) -> Evento:
    """Usa sessão dedicada, sem alterações pendentes; o chamador não repete o commit."""
    try:
        evento = Evento(**dados.model_dump())
        db.add(evento)
        db.commit()
    except Exception:
        db.rollback()
        raise

    # Uma falha na leitura após o commit não desfaz a gravação confirmada.
    db.refresh(evento)
    return evento


def listar_eventos(db: Session) -> list[Evento]:
    consulta = select(Evento).order_by(Evento.data, Evento.inicio, Evento.id)
    return list(db.scalars(consulta).all())


def buscar_evento_por_id(db: Session, evento_id: int) -> Evento | None:
    return db.get(Evento, evento_id)
