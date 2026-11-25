"""Apaga associações de alunos a turmas que já foram removidas.

Antes desta revisão, remover uma turma deixava as associações dos alunos apontando para ela, o que
causava erro 500 na lista e na ficha do aluno. Como o SQLite reaproveita o id da turma removida,
a associação também passaria a valer para a próxima turma cadastrada.
"""

from alembic import op

revision = "0008_limpa_associacoes_orfas"
down_revision = "0007_versao_do_termo"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("DELETE FROM aluno_turmas WHERE turma_id NOT IN (SELECT id FROM turmas)")


def downgrade() -> None:
    # As associações apagadas apontavam para turmas inexistentes; não há o que restaurar.
    pass
