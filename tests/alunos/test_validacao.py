"""Formatos dos campos da ficha do aluno (backend/alunos/validacao.py)."""
from datetime import date

import pytest

from backend.alunos import validacao


@pytest.mark.parametrize(
    "digitado, esperado",
    [
        ("61999990101", "(61) 99999-0101"),
        ("(61) 99999-0101", "(61) 99999-0101"),
        ("061999990101", "(61) 99999-0101"),
        ("6133334444", "(61) 3333-4444"),
        ("0 61 3333-4444", "(61) 3333-4444"),
    ],
)
def test_telefone_valido_e_padronizado(digitado, esperado):
    assert validacao.telefone(digitado) == (esperado, None)


@pytest.mark.parametrize(
    "digitado",
    ["9999-0101", "61 9999", "(61) 99999-01019", "(10) 99999-0101", "(61) 89999-0101", "(61) 1333-4444"],
)
def test_telefone_invalido(digitado):
    _, erro = validacao.telefone(digitado)

    assert erro


def test_celular_nao_aceita_fixo():
    _, erro = validacao.telefone("(61) 3333-4444", so_celular=True)

    assert "celular" in erro.lower()


def test_cpf_valido_e_padronizado():
    assert validacao.cpf("52998224725") == ("529.982.247-25", None)


@pytest.mark.parametrize("digitado", ["123.456.789-00", "111.111.111-11", "5299822472", "529.982.247-255"])
def test_cpf_invalido(digitado):
    _, erro = validacao.cpf(digitado)

    assert erro


def test_cep():
    assert validacao.cep("73355001") == ("73355-001", None)
    assert validacao.cep("7335500")[1]


@pytest.mark.parametrize("nome", ["Ana Clara de Oliveira", "João D'Ávila", "Maria-Eduarda Souza"])
def test_nome_completo_valido(nome):
    assert validacao.nome_completo(nome) == (nome, None)


@pytest.mark.parametrize("nome", ["Ana", "Ana 2", "Ana@Souza"])
def test_nome_completo_invalido(nome):
    assert validacao.nome_completo(nome)[1]


@pytest.mark.parametrize("texto", ["não aplicável", "Nao aplicavel", "N/A"])
def test_reconhece_nao_aplicavel(texto):
    assert validacao.e_nao_aplicavel(texto)


def test_datas():
    hoje = date(2026, 11, 18)

    assert validacao.data_nascimento(date(2030, 1, 1), hoje)
    assert validacao.data_nascimento(date(2012, 5, 18), hoje) is None
    assert validacao.data_inicio(date(2010, 1, 1), date(2012, 5, 18), hoje)
    assert validacao.data_inicio(date(2026, 2, 2), date(2012, 5, 18), hoje) is None
