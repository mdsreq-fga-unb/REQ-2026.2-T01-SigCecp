"""Serviços de turmas e da associação de alunos (backend/turmas/services.py)."""
from datetime import time

import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool

from backend.turmas.models import Turma
from backend.turmas.schemas import TurmaCreate
from backend.turmas.services import (
    alunos_mock,
    associar_alunos,
    atualizar_turma,
    buscar_turma,
    buscar_turma_por_id,
    criar_turma,
    deletar_turma,
    listar_alunos,
    listar_turmas,
)


@pytest.fixture
def sessoes(tmp_path):
    engine = create_engine(f"sqlite:///{(tmp_path / 'turmas.db').as_posix()}", poolclass=NullPool)
    Turma.__table__.create(engine)
    yield sessionmaker(bind=engine)
    engine.dispose()


def turma(modalidade="Judô", dias=("segunda", "quarta"), inicio="14:00", termino="15:00"):
    return TurmaCreate(modalidade=modalidade, dias=list(dias), inicio=inicio, termino=termino)


# ---------- Cadastrar ----------

def test_criar_turma_e_ler_em_nova_sessao(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id

    with sessoes() as db:
        encontrada = buscar_turma_por_id(db, turma_id)

        assert encontrada.modalidade == "Judô"
        assert encontrada.dias == ["segunda", "quarta"]
        assert encontrada.inicio == time(14, 0)
        assert encontrada.termino == time(15, 0)


def test_turma_nova_recebe_os_alunos_mock(sessoes):
    with sessoes() as db:
        criada = criar_turma(db, turma())

        assert criada.alunos == alunos_mock


def test_turma_igual_e_recusada_com_409(sessoes):
    with sessoes() as db:
        criar_turma(db, turma())

        with pytest.raises(HTTPException) as erro:
            criar_turma(db, turma())

        assert erro.value.status_code == 409


def test_turma_igual_com_dias_em_outra_ordem_tambem_e_recusada(sessoes):
    with sessoes() as db:
        criar_turma(db, turma(dias=("segunda", "quarta")))

        with pytest.raises(HTTPException) as erro:
            criar_turma(db, turma(dias=("quarta", "segunda")))

        assert erro.value.status_code == 409


@pytest.mark.parametrize(
    "diferenca",
    [
        {"modalidade": "Capoeira"},
        {"dias": ("sexta",)},
        {"inicio": "15:00", "termino": "16:00"},
    ],
)
def test_turma_com_algum_dado_diferente_e_aceita(sessoes, diferenca):
    with sessoes() as db:
        criar_turma(db, turma())
        criar_turma(db, turma(**diferenca))

        assert len(listar_turmas(db)) == 2


# ---------- Consultar ----------

def test_listar_turmas_vazio(sessoes):
    with sessoes() as db:
        assert listar_turmas(db) == []


def test_listar_turmas_em_ordem_de_cadastro(sessoes):
    with sessoes() as db:
        criar_turma(db, turma(modalidade="Judô"))
        criar_turma(db, turma(modalidade="Capoeira"))
        criar_turma(db, turma(modalidade="Karatê"))

        assert [t.modalidade for t in listar_turmas(db)] == ["Judô", "Capoeira", "Karatê"]


def test_buscar_turma_inexistente(sessoes):
    with sessoes() as db:
        assert buscar_turma_por_id(db, 99) is None

        with pytest.raises(HTTPException) as erro:
            buscar_turma(db, 99)

        assert erro.value.status_code == 404


# ---------- Editar ----------

def test_atualizar_turma(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id
        atualizar_turma(db, turma_id, turma(modalidade="Judô infantil", dias=("sabado",), inicio="10:00", termino="11:00"))

    with sessoes() as db:
        atualizada = buscar_turma(db, turma_id)

        assert atualizada.modalidade == "Judô infantil"
        assert atualizada.dias == ["sabado"]
        assert atualizada.inicio == time(10, 0)


def test_atualizar_para_dados_de_outra_turma_e_recusado(sessoes):
    with sessoes() as db:
        criar_turma(db, turma(modalidade="Judô"))
        outra_id = criar_turma(db, turma(modalidade="Capoeira")).id

        with pytest.raises(HTTPException) as erro:
            atualizar_turma(db, outra_id, turma(modalidade="Judô"))

        assert erro.value.status_code == 409


def test_atualizar_mantendo_os_proprios_dados_e_aceito(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id

        atualizada = atualizar_turma(db, turma_id, turma())

        assert atualizada.id == turma_id


def test_atualizar_turma_inexistente(sessoes):
    with sessoes() as db:
        with pytest.raises(HTTPException) as erro:
            atualizar_turma(db, 99, turma())

        assert erro.value.status_code == 404


@pytest.mark.xfail(
    reason="Pendência do readme (9.5): editar a turma grava o campo alunos vazio do formulário.",
    strict=True,
)
def test_editar_turma_preserva_os_alunos(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id
        atualizar_turma(db, turma_id, turma(termino="16:00"))

    with sessoes() as db:
        assert buscar_turma(db, turma_id).alunos == alunos_mock


# ---------- Remover ----------

def test_deletar_turma(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id
        deletar_turma(db, turma_id)

    with sessoes() as db:
        assert buscar_turma_por_id(db, turma_id) is None


def test_deletar_turma_inexistente(sessoes):
    with sessoes() as db:
        with pytest.raises(HTTPException) as erro:
            deletar_turma(db, 99)

        assert erro.value.status_code == 404


# ---------- Alunos da turma ----------

def test_listar_alunos_da_turma(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id

        assert listar_alunos(db, turma_id) == alunos_mock


def test_associar_alunos_grava_a_lista(sessoes):
    with sessoes() as db:
        turma_id = criar_turma(db, turma()).id
        associar_alunos(db, turma_id, ["Ana Clara de Oliveira Santos"])

    with sessoes() as db:
        assert listar_alunos(db, turma_id) == ["Ana Clara de Oliveira Santos"]


def test_associar_alunos_em_turma_inexistente(sessoes):
    with sessoes() as db:
        with pytest.raises(HTTPException) as erro:
            associar_alunos(db, 99, ["Ana"])

        assert erro.value.status_code == 404
