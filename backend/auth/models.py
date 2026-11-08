from datetime import datetime

from sqlalchemy import Boolean, DateTime, ForeignKey, Integer, String, func, true
from sqlalchemy.orm import Mapped, mapped_column

from backend.auth.tempo import agora
from backend.database import Base


class Administrador(Base):

    __tablename__ = "administradores"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    usuario: Mapped[str] = mapped_column(String(50), nullable=False, unique=True, index=True)

    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, server_default=true())

    tentativas_falhas: Mapped[int] = mapped_column(Integer, nullable=False, default=0, server_default="0")
    bloqueado_ate: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)

    criado_em: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), nullable=False,
    )
    ultimo_login_em: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)


class RefreshToken(Base):

    __tablename__ = "refresh_tokens_admin"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    administrador_id: Mapped[int] = mapped_column(
        ForeignKey("administradores.id", ondelete="CASCADE"), nullable=False, index=True,
    )
    familia: Mapped[str] = mapped_column(String(32), nullable=False, index=True)
    token_hash: Mapped[str] = mapped_column(String(64), nullable=False, unique=True, index=True)

    criado_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False, default=agora)
    expira_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    
    sessao_iniciada_em: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=False)

    usado_em: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    revogado_em: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
