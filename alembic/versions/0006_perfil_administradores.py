"""Nome e perfil das contas: Root gerencia coordenadores; Coordenador usa a área administrativa.

As contas que já existem foram criadas pelo terminal (RN21) e passam a ser Root.
"""

from alembic import op
import sqlalchemy as sa

revision = "0006_perfil_administradores"
down_revision = "0005_cria_alunos"
branch_labels = None
depends_on = None


def upgrade() -> None:
    with op.batch_alter_table("administradores") as tabela:
        tabela.add_column(sa.Column("nome", sa.String(200), nullable=True))
        tabela.add_column(sa.Column("perfil", sa.String(20), nullable=False, server_default="coordenador"))
    op.execute("UPDATE administradores SET perfil = 'root'")


def downgrade() -> None:
    with op.batch_alter_table("administradores") as tabela:
        tabela.drop_column("perfil")
        tabela.drop_column("nome")
