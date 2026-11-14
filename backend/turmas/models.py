from datetime import time

from sqlalchemy import JSON, Integer, String, Time
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Turma(Base):
    __tablename__ = "turmas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    modalidade: Mapped[str] = mapped_column(String(120), nullable=False)
    dias: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    inicio: Mapped[time] = mapped_column(Time, nullable=False)
    termino: Mapped[time] = mapped_column(Time, nullable=False)