"""Ficha do aluno (RF21 a RF24) e associação aluno–turma com histórico (RF06, DEC35).

A coluna turmas.alunos guardava a lista de nomes de exemplo usada antes do cadastro de
alunos; a associação passa a ficar na tabela aluno_turmas.
"""

from alembic import op
import sqlalchemy as sa

revision = "0005_cria_alunos"
down_revision = "a875dcabae5a"
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "alunos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("nome", sa.String(200), nullable=False),
        sa.Column("data_inicio", sa.Date(), nullable=False),
        sa.Column("documento_identificacao", sa.String(60), nullable=False),
        sa.Column("nome_mae", sa.String(200), nullable=False),
        sa.Column("telefone_mae", sa.String(30), nullable=False),
        sa.Column("telefone_pai", sa.String(30), nullable=True),
        sa.Column("celular", sa.String(30), nullable=False),
        sa.Column("telefone_emergencia", sa.String(30), nullable=True),
        sa.Column("tipo_escola", sa.String(20), nullable=False),
        sa.Column("nome_escola", sa.String(200), nullable=True),
        sa.Column("graduacao", sa.String(60), nullable=False),
        sa.Column("data_nascimento", sa.Date(), nullable=True),
        sa.Column("cpf", sa.String(20), nullable=True),
        sa.Column("endereco", sa.String(255), nullable=True),
        sa.Column("cidade", sa.String(100), nullable=True),
        sa.Column("cep", sa.String(15), nullable=True),
        sa.Column("nome_pai", sa.String(200), nullable=True),
        sa.Column("telefone_residencial", sa.String(30), nullable=True),
        sa.Column("nome_contato_urgencia", sa.String(200), nullable=True),
        sa.Column("responsavel_nome", sa.String(200), nullable=True),
        sa.Column("responsavel_cpf", sa.String(20), nullable=True),
        sa.Column("responsavel_identidade", sa.String(60), nullable=True),
        sa.Column("saida_aluno", sa.String(20), nullable=True),
        sa.Column("acompanhante", sa.String(200), nullable=True),
        sa.Column("turno_escolar", sa.String(20), nullable=True),
        sa.Column("problema_saude", sa.Boolean(), nullable=False),
        sa.Column("descricao_saude", sa.Text(), nullable=True),
        sa.Column("questionario", sa.Text(), nullable=False),
        sa.Column("termo_aceito_em", sa.DateTime(), nullable=False),
        sa.Column("ativo", sa.Boolean(), nullable=False),
        sa.Column("inativado_em", sa.DateTime(), nullable=True),
        sa.Column("criado_em", sa.DateTime(), nullable=False),
        sa.Column("atualizado_em", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_alunos_id", "alunos", ["id"])

    op.create_table(
        "aluno_turmas",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("aluno_id", sa.Integer(), sa.ForeignKey("alunos.id"), nullable=False),
        sa.Column("turma_id", sa.Integer(), sa.ForeignKey("turmas.id"), nullable=False),
        sa.Column("inicio", sa.DateTime(), nullable=False),
        sa.Column("fim", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_aluno_turmas_aluno_id", "aluno_turmas", ["aluno_id"])
    op.create_index("ix_aluno_turmas_turma_id", "aluno_turmas", ["turma_id"])

    op.create_table(
        "aluno_documentos",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("aluno_id", sa.Integer(), sa.ForeignKey("alunos.id"), nullable=False),
        sa.Column("tipo", sa.String(40), nullable=False),
        sa.Column("nome_original", sa.String(255), nullable=False),
        sa.Column("caminho", sa.String(255), nullable=False),
        sa.Column("content_type", sa.String(100), nullable=False),
        sa.Column("enviado_em", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index("ix_aluno_documentos_aluno_id", "aluno_documentos", ["aluno_id"])

    with op.batch_alter_table("turmas") as tabela:
        tabela.drop_column("alunos")


def downgrade() -> None:
    with op.batch_alter_table("turmas") as tabela:
        tabela.add_column(sa.Column("alunos", sa.JSON(), nullable=False, server_default="[]"))

    op.drop_index("ix_aluno_documentos_aluno_id", table_name="aluno_documentos")
    op.drop_table("aluno_documentos")
    op.drop_index("ix_aluno_turmas_turma_id", table_name="aluno_turmas")
    op.drop_index("ix_aluno_turmas_aluno_id", table_name="aluno_turmas")
    op.drop_table("aluno_turmas")
    op.drop_index("ix_alunos_id", table_name="alunos")
    op.drop_table("alunos")
