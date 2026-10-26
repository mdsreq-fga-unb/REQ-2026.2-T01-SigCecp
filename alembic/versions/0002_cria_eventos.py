"""Tabela de eventos."""

from alembic import op
import sqlalchemy as sa

revision = "0002_cria_eventos"
down_revision = "0001_baseline_publicacoes"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "eventos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("titulo", sa.String(120), nullable=False),
        sa.Column("subtitulo", sa.String(120), nullable=False),
        sa.Column("nome", sa.String(120), nullable=False),
        sa.Column("data", sa.Date(), nullable=False),
        sa.Column("inicio", sa.Time(), nullable=False),
        sa.Column("termino", sa.Time(), nullable=False),
        sa.Column("local", sa.String(255), nullable=False),
        sa.Column("descricao", sa.Text(), nullable=False),
        sa.Column("alimentacao", sa.Boolean(), nullable=False),
        sa.Column("pesagem", sa.String(13), nullable=False),
        sa.Column("cobrado", sa.Boolean(), nullable=False),
        sa.Column("valor", sa.Numeric(12, 2), nullable=True),
        sa.Column("data_limite_pagamento", sa.Date(), nullable=True),
        sa.Column("meio_pagamento", sa.String(255), nullable=True),
        sa.CheckConstraint(
            "pesagem IN ('sim', 'nao', 'nao_se_aplica')",
            name="ck_eventos_pesagem",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_eventos_id", "eventos", ["id"])


def downgrade() -> None:
    op.drop_index("ix_eventos_id", table_name="eventos")
    op.drop_table("eventos")
