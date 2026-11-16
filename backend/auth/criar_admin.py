"""Cria o administrador (ou redefine a senha dele) no banco do projeto

Uso, na raiz do projeto e com o ambiente virtual (venv) ativo

    python -m backend.auth.criar_admin --usuario CECP0001
    python -m backend.auth.criar_admin --usuario CECP0001 --redefinir-senha

"""

import argparse
import getpass
import sys

from sqlalchemy import select
from sqlalchemy.exc import OperationalError, ProgrammingError

from backend import database
from backend.auth import security, services
from backend.auth.models import Administrador


def _pedir_senha() -> str:
    senha = getpass.getpass("Senha: ")
    if senha != getpass.getpass("Confirme a senha: "):
        raise SystemExit("As senhas não conferem.")
    return senha


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Cria ou redefine a senha do administrador.")
    parser.add_argument("--usuario", required=True, help="Nome de usuário (ex.: CECP0001).")
    parser.add_argument(
        "--redefinir-senha", action="store_true",
        help="Redefine a senha de um administrador existente e encerra suas sessões.",
    )
    args = parser.parse_args(argv)

    nome = services.normalizar_usuario(args.usuario)
    db = database.SessionLocal()
    try:
        try:
            existente = db.execute(
                select(Administrador).where(Administrador.usuario == nome)
            ).scalar_one_or_none()
        except (OperationalError, ProgrammingError):
            print(
                "Tabela 'administradores' não encontrada. Aplique as migrações antes:\n"
                "    python -m alembic upgrade head",
                file=sys.stderr,
            )
            return 1

        if existente and not args.redefinir_senha:
            print(f"O usuário '{nome}' já existe. Use --redefinir-senha para trocar a senha.", file=sys.stderr)
            return 1
        if not existente and args.redefinir_senha:
            print(f"O usuário '{nome}' não existe.", file=sys.stderr)
            return 1

        senha = _pedir_senha()
        try:
            security.validar_politica_senha(senha, nome)
            if existente:
                services.redefinir_senha(db, existente, senha)
                print(f"Senha de '{nome}' redefinida; as sessões abertas foram encerradas.")
            else:
                services.criar_administrador(db, nome, senha)
                print(f"Administrador '{nome}' criado.")
        except (security.SenhaInvalida, ValueError) as erro:
            print(f"Erro: {erro}", file=sys.stderr)
            return 1
        return 0
    finally:
        db.close()


if __name__ == "__main__":
    raise SystemExit(main())
