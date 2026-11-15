"""Validação dos dados de turma (TurmaCreate)."""
from datetime import time, timezone

import pytest
from pydantic import ValidationError

from backend.turmas.schemas import TurmaCreate


def dados(**alteracoes):
    base = {
        "modalidade": "Judô",
        "dias": ["segunda", "quarta"],
        "inicio": "14:00",
        "termino": "15:00",
    }
    base.update(alteracoes)
    return base


def test_aceita_turma_valida():
    turma = TurmaCreate(**dados())

    assert turma.modalidade == "Judô"
    assert turma.dias == ["segunda", "quarta"]
    assert turma.inicio == time(14, 0)
    assert turma.termino == time(15, 0)


def test_alunos_comeca_vazio_quando_nao_informado():
    assert TurmaCreate(**dados()).alunos == []


def test_modalidade_vazia_e_recusada():
    with pytest.raises(ValidationError):
        TurmaCreate(**dados(modalidade=""))


def test_modalidade_acima_de_120_caracteres_e_recusada():
    with pytest.raises(ValidationError):
        TurmaCreate(**dados(modalidade="J" * 121))


def test_exige_ao_menos_um_dia():
    with pytest.raises(ValidationError):
        TurmaCreate(**dados(dias=[]))


def test_dia_fora_da_semana_e_recusado():
    with pytest.raises(ValidationError):
        TurmaCreate(**dados(dias=["feriado"]))


@pytest.mark.parametrize("campo", ["modalidade", "dias", "inicio", "termino"])
def test_campos_obrigatorios(campo):
    valores = dados()
    del valores[campo]

    with pytest.raises(ValidationError):
        TurmaCreate(**valores)


def test_horario_com_fuso_e_recusado():
    with pytest.raises(ValidationError):
        TurmaCreate(**dados(inicio=time(14, 0, tzinfo=timezone.utc)))


def test_horario_com_fracao_de_segundo_e_recusado():
    with pytest.raises(ValidationError):
        TurmaCreate(**dados(termino=time(15, 0, 0, 500)))
