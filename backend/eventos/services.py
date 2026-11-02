
import logging
from datetime import datetime
from zoneinfo import ZoneInfo

from fastapi import HTTPException, status, UploadFile
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.eventos.models import Evento
from backend.eventos.schemas import EventoCreate
from backend.eventos.media import (
    salvar_midia,
    remover_midia,
    TIPOS_IMAGEM,
    TIPOS_VIDEO,
)

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


def criar_evento(
    db: Session,
    dados: EventoCreate,
    imagem: UploadFile | None = None,
    video: UploadFile | None = None,
) -> Evento:
    """Cria um novo evento e salva suas mídias."""

    caminhos_salvos = []

    try:
        caminho_imagem = salvar_midia(imagem, TIPOS_IMAGEM)
        caminho_video = salvar_midia(video, TIPOS_VIDEO)

        if caminho_imagem:
            caminhos_salvos.append(caminho_imagem)

        if caminho_video:
            caminhos_salvos.append(caminho_video)

        evento = Evento(
            **dados.model_dump(),
            imagem=caminho_imagem,
            video=caminho_video,
        )

        db.add(evento)
        db.commit()
        db.refresh(evento)

        return evento

    except Exception:
        db.rollback()

        for caminho in caminhos_salvos:
            remover_midia(caminho)

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
    imagem: UploadFile | None = None,
    video: UploadFile | None = None,
) -> Evento:
    """Atualiza os dados e as mídias de um evento."""
    evento = buscar_evento(db, evento_id)

    caminhos_salvos = []

    try:
        for campo, valor in dados.model_dump().items():
            setattr(evento, campo, valor)

        if imagem and imagem.filename:
            nova_imagem = salvar_midia(imagem, TIPOS_IMAGEM)

            if nova_imagem:
                caminhos_salvos.append(nova_imagem)
                remover_midia(evento.imagem)
                evento.imagem = nova_imagem

        if video and video.filename:
            novo_video = salvar_midia(video, TIPOS_VIDEO)

            if novo_video:
                caminhos_salvos.append(novo_video)
                remover_midia(evento.video)
                evento.video = novo_video

        db.commit()
        db.refresh(evento)

    except Exception:
        db.rollback()

        for caminho in caminhos_salvos:
            remover_midia(caminho)

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


