"""Estrutura de publicações anterior às migrações."""

from alembic import op
import sqlalchemy as sa

revision = "0001_baseline_publicacoes"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "publicacoes",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("titulo", sa.String(200), nullable=False),
        sa.Column("texto", sa.Text(), nullable=True),
        sa.Column(
            "criada_em", sa.DateTime(timezone=True),
            server_default=sa.func.now(), nullable=False,
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_publicacoes_id", "publicacoes", ["id"])
    op.create_table(
        "publicacao_midias",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("publicacao_id", sa.Integer(), nullable=False),
        sa.Column("caminho", sa.String(500), nullable=False),
        sa.Column("tipo", sa.String(20), nullable=False),
        sa.Column("nome_original", sa.String(255), nullable=False),
        sa.ForeignKeyConstraint(["publicacao_id"], ["publicacoes.id"], ondelete="CASCADE"),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_publicacao_midias_id", "publicacao_midias", ["id"])


def downgrade() -> None:
    op.drop_index("ix_publicacao_midias_id", table_name="publicacao_midias")
    op.drop_table("publicacao_midias")
    op.drop_index("ix_publicacoes_id", table_name="publicacoes")
    op.drop_table("publicacoes")
