"""Remover turma passa a desativá-la, preservando o histórico de vínculos dos alunos (RN01, DEC35).

Antes, a remoção apagava a turma e todas as associações a ela, abertas e encerradas.
"""

from alembic import op
import sqlalchemy as sa

revision = "0009_turma_ativa"
down_revision = "0008_limpa_associacoes_orfas"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("turmas") as tabela:
        tabela.add_column(sa.Column("ativa", sa.Boolean(), nullable=False, server_default=sa.true()))


def downgrade() -> None:
    with op.batch_alter_table("turmas") as tabela:
        tabela.drop_column("ativa")
