from datetime import date, time
from decimal import Decimal

from sqlalchemy import Boolean, CheckConstraint, Date, Integer, Numeric, String, Text, Time
from sqlalchemy.orm import Mapped, mapped_column

from backend.database import Base


class Evento(Base):
    __tablename__ = "eventos"
    __table_args__ = (
        CheckConstraint(
            "pesagem IN ('sim', 'nao', 'nao_se_aplica')",
            name="ck_eventos_pesagem",
        ),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String(120), nullable=False)
    subtitulo: Mapped[str] = mapped_column(String(120), nullable=False)
    nome: Mapped[str] = mapped_column(String(120), nullable=False)
    data: Mapped[date] = mapped_column(Date, nullable=False)
    inicio: Mapped[time] = mapped_column(Time, nullable=False)
    termino: Mapped[time] = mapped_column(Time, nullable=False)
    local: Mapped[str] = mapped_column(String(255), nullable=False)
    descricao: Mapped[str] = mapped_column(Text, nullable=False)
    alimentacao: Mapped[bool] = mapped_column(Boolean, nullable=False)
    pesagem: Mapped[str] = mapped_column(String(13), nullable=False)
    cobrado: Mapped[bool] = mapped_column(Boolean, nullable=False)
    valor: Mapped[Decimal | None] = mapped_column(Numeric(12, 2), nullable=True)
    data_limite_pagamento: Mapped[date | None] = mapped_column(Date, nullable=True)
    meio_pagamento: Mapped[str | None] = mapped_column(String(255), nullable=True)
