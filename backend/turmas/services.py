import logging

from fastapi import HTTPException, status
from sqlalchemy import select
from sqlalchemy.orm import Session

from backend.alunos.models import AlunoTurma
from backend.alunos.services import agora
from backend.turmas.models import Turma
from backend.turmas.schemas import TurmaCreate

logger = logging.getLogger(__name__)


def _existe_turma_igual(
    db: Session, dados: TurmaCreate, ignorar_id: int | None = None
) -> bool:
    """Verifica se já existe turma com mesma modalidade, dias e horários."""
    consulta = select(Turma).where(
        Turma.ativa.is_(True),
        Turma.modalidade == dados.modalidade,
        Turma.inicio == dados.inicio,
        Turma.termino == dados.termino,
    )
    for turma in db.scalars(consulta):
        if turma.id != ignorar_id and sorted(turma.dias) == sorted(dados.dias):
            return True
    return False


def criar_turma(db: Session, dados: TurmaCreate) -> Turma:
    if _existe_turma_igual(db, dados):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma turma com essa modalidade, esses dias e esses horários.",
        )

    turma = Turma(**dados.model_dump())

    try:
        db.add(turma)
        db.commit()
        db.refresh(turma)
        return turma
    except Exception:
        db.rollback()
        logger.exception("Erro ao criar turma")
        raise


def listar_turmas(db: Session) -> list[Turma]:
    consulta = select(Turma).where(Turma.ativa.is_(True)).order_by(Turma.id)
    return list(db.scalars(consulta).all())


def buscar_turma_por_id(db: Session, turma_id: int) -> Turma | None:
    return db.get(Turma, turma_id)


def buscar_turma(db: Session, turma_id: int) -> Turma:
    """Busca uma turma ativa ou retorna erro 404. Turma removida não é editada nem recebe alunos."""
    turma = db.get(Turma, turma_id)

    if turma is None or not turma.ativa:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Turma não encontrada",
        )

    return turma


def atualizar_turma(db: Session, turma_id: int, dados: TurmaCreate) -> Turma:
    """Atualiza os dados de uma turma."""
    turma = buscar_turma(db, turma_id)

    if _existe_turma_igual(db, dados, ignorar_id=turma_id):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Já existe uma turma com essa modalidade, esses dias e esses horários.",
        )

    for campo, valor in dados.model_dump().items():
        setattr(turma, campo, valor)

    try:
        db.commit()
        db.refresh(turma)
        return turma
    except Exception:
        db.rollback()
        logger.exception("Erro ao atualizar turma")
        raise


def deletar_turma(db: Session, turma_id: int) -> None:
    """Remove a turma da lista sem apagar o histórico: encerra os vínculos abertos e desativa a turma (RN01, DEC35)."""
    turma = buscar_turma(db, turma_id)
    quando = agora()

    try:
        abertos = db.scalars(select(AlunoTurma).where(AlunoTurma.turma_id == turma.id, AlunoTurma.fim.is_(None)))
        for associacao in abertos:
            associacao.fim = quando
        turma.ativa = False
        db.commit()
    except Exception:
        db.rollback()
        logger.exception("Erro ao deletar turma")
        raise
