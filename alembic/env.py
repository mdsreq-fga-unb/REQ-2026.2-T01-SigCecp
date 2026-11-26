from alembic import context

from backend.database import Base, DATABASE_URL, engine
# Os models são importados para registrar as tabelas em Base.metadata
from backend.auth import models as auth_models  # noqa: F401
from backend.eventos import models as eventos_models  # noqa: F401
from backend.publicacoes import models as publicacoes_models  # noqa: F401
from backend.turmas import models as turmas_models  # noqa: F401
from backend.alunos import models as alunos_models  # noqa: F401

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
        compare_type=True,
        render_as_batch=True,
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    with engine.connect() as connection:
        if connection.dialect.name == "sqlite":
            # O app ativa as chaves estrangeiras em cada conexão (backend/database.py).
            # Nas migrações elas ficam desligadas: o modo em lote recria tabelas
            # (DROP + CREATE), o que falharia com tabelas que têm dependentes.
            connection.exec_driver_sql("PRAGMA foreign_keys=OFF")
            connection.commit()

        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
            render_as_batch=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
