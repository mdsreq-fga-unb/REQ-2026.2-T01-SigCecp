"""Administradores e refresh tokens da área administrativa."""

from alembic import op
import sqlalchemy as sa

revision = "0003_cria_administradores"
down_revision = "926c0efbdcbb"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "administradores",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("usuario", sa.String(50), nullable=False),
        sa.Column("senha_hash", sa.String(255), nullable=False),
        sa.Column("ativo", sa.Boolean(), server_default=sa.true(), nullable=False),
        sa.Column("tentativas_falhas", sa.Integer(), server_default="0", nullable=False),
        sa.Column("bloqueado_ate", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "criado_em", sa.DateTime(timezone=True),
            server_default=sa.func.now(), nullable=False,
        ),
        sa.Column("ultimo_login_em", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_administradores_usuario", "administradores", ["usuario"], unique=True)

    op.create_table(
        "refresh_tokens_admin",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("administrador_id", sa.Integer(), nullable=False),
        sa.Column("familia", sa.String(32), nullable=False),
        sa.Column("token_hash", sa.String(64), nullable=False),
        sa.Column("criado_em", sa.DateTime(timezone=True), nullable=False),
        sa.Column("expira_em", sa.DateTime(timezone=True), nullable=False),
        sa.Column("sessao_iniciada_em", sa.DateTime(timezone=True), nullable=False),
        sa.Column("usado_em", sa.DateTime(timezone=True), nullable=True),
        sa.Column("revogado_em", sa.DateTime(timezone=True), nullable=True),
        sa.ForeignKeyConstraint(["administrador_id"], ["administradores.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_refresh_tokens_admin_administrador_id", "refresh_tokens_admin", ["administrador_id"])
    op.create_index("ix_refresh_tokens_admin_familia", "refresh_tokens_admin", ["familia"])
    op.create_index("ix_refresh_tokens_admin_token_hash", "refresh_tokens_admin", ["token_hash"], unique=True)


def downgrade() -> None:
    op.drop_index("ix_refresh_tokens_admin_token_hash", table_name="refresh_tokens_admin")
    op.drop_index("ix_refresh_tokens_admin_familia", table_name="refresh_tokens_admin")
    op.drop_index("ix_refresh_tokens_admin_administrador_id", table_name="refresh_tokens_admin")
    op.drop_table("refresh_tokens_admin")
    op.drop_index("ix_administradores_usuario", table_name="administradores")
    op.drop_table("administradores")
