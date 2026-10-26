
from datetime import datetime
from sqlalchemy import (
    DateTime,
    ForeignKey,
    Integer,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.database import Base


class Publicacao(Base):
    __tablename__ = "publicacoes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    titulo: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )
    texto: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )
    criada_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    midias: Mapped[list["PublicacaoMidia"]] = relationship(
        back_populates="publicacao",
        cascade="all, delete-orphan",
    )


class PublicacaoMidia(Base):
    __tablename__ = "publicacao_midias"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )
    publicacao_id: Mapped[int] = mapped_column(
        ForeignKey("publicacoes.id", ondelete="CASCADE"),
        nullable=False,
    )
    caminho: Mapped[str] = mapped_column(
        String(500),
        nullable=False,
    )
    tipo: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
    )
    nome_original: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    publicacao: Mapped["Publicacao"] = relationship(
        back_populates="midias",
    )
