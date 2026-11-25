import os
import subprocess
import sys
from pathlib import Path

from alembic.config import Config
from alembic.script import ScriptDirectory
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import Session

from backend.eventos.models import Evento
from backend.publicacoes.models import Publicacao, PublicacaoMidia
from backend.alunos.models import Aluno, AlunoDocumento, AlunoTurma
from backend.turmas.models import Turma

ROOT = Path(__file__).resolve().parent.parent.parent

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

    assert resultado.returncode == 0, resultado.stdout + resultado.stderr
def verificar_estrutura(engine):
    inspetor = inspect(engine)
    assert set(inspetor.get_table_names()) == {
        "alembic_version", "publicacoes", "publicacao_midias", "eventos",
        "administradores", "refresh_tokens_admin", "turmas",
        "alunos", "aluno_turmas", "aluno_documentos",
    }
    for modelo in (Publicacao, PublicacaoMidia, Evento, Turma, Aluno, AlunoTurma, AlunoDocumento):
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
            version = connection.exec_driver_sql(
                "SELECT version_num FROM alembic_version"
            ).scalar_one()
            head = ScriptDirectory.from_config(Config(str(ROOT / "alembic.ini"))).get_current_head()
            assert version == head
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


def test_migracao_apaga_associacoes_a_turmas_removidas(tmp_path):
    url = f"sqlite:///{(tmp_path / 'orfas.db').as_posix()}"
    executar_alembic(url, "upgrade", "0007_versao_do_termo")

    engine = create_engine(url)
    try:
        with engine.begin() as conexao:
            conexao.exec_driver_sql(
                "INSERT INTO turmas (id, modalidade, dias, inicio, termino) VALUES (2, 'Judô', '[\"segunda\"]', '14:00:00', '15:00:00')"
            )
            conexao.exec_driver_sql(
                "INSERT INTO alunos (id, nome, data_inicio, documento_identificacao, nome_mae, telefone_mae, celular,"
                " tipo_escola, graduacao, problema_saude, questionario, termo_aceito_em, termo_versao, ativo, criado_em)"
                " VALUES (1, 'Ana', '2026-01-01', 'RG', 'Maria', '61999990101', '61999990101', 'publica', 'Branca', 0,"
                " 'x', '2026-01-01', '1.0', 1, '2026-01-01')"
            )
            conexao.exec_driver_sql(
                "INSERT INTO aluno_turmas (aluno_id, turma_id, inicio) VALUES (1, 1, '2026-01-01'), (1, 2, '2026-02-01')"
            )

        executar_alembic(url, "upgrade", "head")

        with engine.connect() as conexao:
            restantes = conexao.exec_driver_sql("SELECT turma_id FROM aluno_turmas").scalars().all()
        assert restantes == [2]
    finally:
        engine.dispose()


def test_upgrade_de_banco_com_turmas_na_0004(tmp_path):
    """A coluna temporária turmas.alunos (NOT NULL) não pode quebrar o upgrade quando já há turmas."""
    url = f"sqlite:///{(tmp_path / 'com_turmas.db').as_posix()}"
    executar_alembic(url, "upgrade", "0004_cria_turmas")

    engine = create_engine(url)
    try:
        with engine.begin() as conexao:
            conexao.exec_driver_sql(
                "INSERT INTO turmas (modalidade, dias, inicio, termino)"
                " VALUES ('Judô', '[\"segunda\"]', '14:00:00', '15:00:00')"
            )

        executar_alembic(url, "upgrade", "head")

        verificar_estrutura(engine)
        with Session(engine) as db:
            [turma] = db.query(Turma).all()
            assert turma.modalidade == "Judô"
            assert turma.ativa is True
    finally:
        engine.dispose()
