import os
import subprocess
import sys
from pathlib import Path

from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session

from backend.eventos.models import Evento
from backend.publicacoes.models import Publicacao, PublicacaoMidia


ROOT = Path(__file__).resolve().parents[1]


def executar_alembic(database_url, *args):
    ambiente = os.environ.copy()
    ambiente["DATABASE_URL"] = database_url
    resultado = subprocess.run(
        [sys.executable, "-m", "alembic", "-c", str(ROOT / "alembic.ini"), *args],
        cwd=ROOT,
        env=ambiente,
        capture_output=True,
        text=True,
        check=False,
    )
    assert resultado.returncode == 0, resultado.stdout + resultado.stderr


def verificar_estrutura(engine):
    inspetor = inspect(engine)
    assert set(inspetor.get_table_names()) == {
        "alembic_version", "publicacoes", "publicacao_midias", "eventos",
    }
    for modelo in (Publicacao, PublicacaoMidia, Evento):
        colunas = {coluna["name"]: coluna for coluna in inspetor.get_columns(modelo.__tablename__)}
        assert set(colunas) == set(modelo.__table__.columns.keys())
        for coluna in modelo.__table__.columns:
            assert colunas[coluna.name]["nullable"] == coluna.nullable

    assert any(
        constraint["name"] == "ck_eventos_pesagem"
        for constraint in inspetor.get_check_constraints("eventos")
    )
    assert any(
        chave["referred_table"] == "publicacoes"
        and chave["options"].get("ondelete") == "CASCADE"
        for chave in inspetor.get_foreign_keys("publicacao_midias")
    )


def test_upgrade_head_em_banco_vazio(tmp_path):
    url = f"sqlite:///{(tmp_path / 'vazio.db').as_posix()}"
    executar_alembic(url, "upgrade", "head")
    executar_alembic(url, "check")

    engine = create_engine(url)
    try:
        verificar_estrutura(engine)
        with engine.connect() as connection:
            assert connection.exec_driver_sql(
                "SELECT version_num FROM alembic_version"
            ).scalar_one() == "0002_cria_eventos"
    finally:
        engine.dispose()


def test_publicacao_e_midia_sobrevivem_a_migracao_de_eventos(tmp_path):
    url = f"sqlite:///{(tmp_path / 'com_publicacao.db').as_posix()}"
    executar_alembic(url, "upgrade", "0001_baseline_publicacoes")

    engine = create_engine(url)
    try:
        assert "eventos" not in inspect(engine).get_table_names()
        with Session(engine) as db:
            publicacao = Publicacao(titulo="Publicação fictícia", texto="Exemplo")
            publicacao.midias.append(PublicacaoMidia(
                caminho="exemplo.png", tipo="imagem", nome_original="exemplo.png",
            ))
            db.add(publicacao)
            db.commit()
            publicacao_id = publicacao.id
            midia_id = publicacao.midias[0].id

        executar_alembic(url, "upgrade", "head")
        executar_alembic(url, "check")

        verificar_estrutura(engine)
        with Session(engine) as db:
            publicacao = db.get(Publicacao, publicacao_id)
            midia = db.get(PublicacaoMidia, midia_id)
            assert publicacao.titulo == "Publicação fictícia"
            assert publicacao.texto == "Exemplo"
            assert midia.publicacao_id == publicacao.id
            assert midia.caminho == "exemplo.png"
    finally:
        engine.dispose()
