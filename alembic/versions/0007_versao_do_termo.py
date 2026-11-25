"""Versão do termo aceito no cadastro do aluno (prova do consentimento, LGPD art. 8º §2).

Os alunos cadastrados antes desta revisão ficam com a versão "anterior".
"""

from alembic import op
import sqlalchemy as sa

revision = "0007_versao_do_termo"
down_revision = "0006_perfil_administradores"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("alunos") as tabela:
        tabela.add_column(sa.Column("termo_versao", sa.String(20), nullable=False, server_default="anterior"))


def downgrade() -> None:
    with op.batch_alter_table("alunos") as tabela:
        tabela.drop_column("termo_versao")
