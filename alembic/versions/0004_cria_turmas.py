"""Turmas da coordenação (RF03)."""

from alembic import op
import sqlalchemy as sa

revision = "0004_cria_turmas"
down_revision = "0003_cria_administradores"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "turmas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("modalidade", sa.String(120), nullable=False),
        sa.Column("dias", sa.JSON(), nullable=False),
        sa.Column("inicio", sa.Time(), nullable=False),
        sa.Column("termino", sa.Time(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_turmas_id", "turmas", ["id"])


def downgrade() -> None:
    op.drop_index("ix_turmas_id", table_name="turmas")
    op.drop_table("turmas")
