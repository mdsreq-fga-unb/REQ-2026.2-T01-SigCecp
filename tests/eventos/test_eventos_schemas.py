from datetime import date, time
from decimal import Decimal

import pytest
from pydantic import ValidationError

from backend.eventos.schemas import EventoCreate


def test_evento_gratuito_valido(dados_evento):
    evento = EventoCreate(**dados_evento)

    assert evento.alimentacao is False
    assert evento.cobrado is False
    assert evento.valor is None
    assert evento.data_limite_pagamento is None
    assert evento.meio_pagamento is None
    assert evento.data == date(2026, 11, 15)
    assert evento.inicio == time(9)


def test_evento_pago_valido_preserva_decimal(dados_evento):
    evento = EventoCreate(**{
        **dados_evento,
        "cobrado": True,
        "valor": "25.50",
        "data_limite_pagamento": "2026-11-10",
        "meio_pagamento": "PIX",
    })

    assert evento.valor == Decimal("25.50")
    assert isinstance(evento.valor, Decimal)
    assert evento.data_limite_pagamento == date(2026, 11, 10)
    assert evento.meio_pagamento == "PIX"


@pytest.mark.parametrize("campo", [
    "titulo", "subtitulo", "nome", "data", "inicio", "termino", "local",
    "descricao", "alimentacao", "pesagem", "cobrado",
])
def test_campo_obrigatorio_ausente(dados_evento, campo):
    dados_evento.pop(campo)

    with pytest.raises(ValidationError) as erro:
        EventoCreate(**dados_evento)

    assert (campo,) in [item["loc"] for item in erro.value.errors()]


@pytest.mark.parametrize("campo", [
    "titulo", "subtitulo", "nome", "local", "descricao",
])
@pytest.mark.parametrize("texto", ["", "   \t  "])
def test_texto_obrigatorio_vazio_ou_so_espacos(dados_evento, campo, texto):
    with pytest.raises(ValidationError, match="deve ser preenchido"):
        EventoCreate(**{**dados_evento, campo: texto})


def test_normaliza_extremidades_sem_alterar_espacos_internos(dados_evento):
    evento = EventoCreate(**{
        **dados_evento,
        "titulo": "  Festival  CECP  ",
        "subtitulo": "  Esporte  para todos  ",
        "nome": "  Festival  esportivo  ",
        "local": "  Quadra  CECP  ",
        "descricao": "  Primeira  linha\nSegunda  linha  ",
        "meio_pagamento": "  PIX  ",
    })

    assert evento.titulo == "Festival  CECP"
    assert evento.subtitulo == "Esporte  para todos"
    assert evento.nome == "Festival  esportivo"
    assert evento.local == "Quadra  CECP"
    assert evento.descricao == "Primeira  linha\nSegunda  linha"
    assert evento.meio_pagamento == "PIX"


@pytest.mark.parametrize("pesagem", ["sim", "nao", "nao_se_aplica"])
def test_opcoes_validas_de_pesagem(dados_evento, pesagem):
    assert EventoCreate(**{**dados_evento, "pesagem": pesagem}).pesagem == pesagem


def test_pesagem_invalida(dados_evento):
    with pytest.raises(ValidationError):
        EventoCreate(**{**dados_evento, "pesagem": "talvez"})


@pytest.mark.parametrize("campo", [
    "valor", "data_limite_pagamento", "meio_pagamento",
])
def test_pagamento_incompleto_em_evento_cobrado(dados_evento, campo):
    pagamento = {
        "valor": "25.50",
        "data_limite_pagamento": "2026-11-10",
        "meio_pagamento": "PIX",
    }
    pagamento.pop(campo)

    with pytest.raises(ValidationError, match="Informe"):
        EventoCreate(**{**dados_evento, "cobrado": True, **pagamento})


def test_meio_de_pagamento_so_com_espacos_em_evento_cobrado(dados_evento):
    with pytest.raises(ValidationError, match="meio de pagamento"):
        EventoCreate(**{
            **dados_evento, "cobrado": True, "valor": "25.50",
            "data_limite_pagamento": "2026-11-10", "meio_pagamento": "   ",
        })


def test_pagamento_informado_em_evento_gratuito_e_preservado(dados_evento):
    evento = EventoCreate(**{
        **dados_evento, "valor": "0.00",
        "data_limite_pagamento": "2026-11-10", "meio_pagamento": "PIX",
    })

    assert evento.cobrado is False
    assert evento.valor == Decimal("0.00")
    assert evento.data_limite_pagamento == date(2026, 11, 10)
    assert evento.meio_pagamento == "PIX"


def test_pagamento_vazio_em_evento_gratuito_vira_ausencia(dados_evento):
    evento = EventoCreate(**{**dados_evento, "meio_pagamento": "  "})

    assert evento.meio_pagamento is None


@pytest.mark.parametrize("campo, limite", [
    ("titulo", 120), ("subtitulo", 120), ("nome", 120),
    ("local", 255), ("descricao", 16000), ("meio_pagamento", 255),
])
def test_limites_de_texto(dados_evento, campo, limite):
    assert len(getattr(EventoCreate(**{**dados_evento, campo: "x" * limite}), campo)) == limite

    with pytest.raises(ValidationError):
        EventoCreate(**{**dados_evento, campo: "x" * (limite + 1)})


@pytest.mark.parametrize("valor", ["1.234", "10000000000.00", "Infinity", "abc"])
def test_valor_fora_da_precisao_ou_invalido(dados_evento, valor):
    with pytest.raises(ValidationError):
        EventoCreate(**{**dados_evento, "valor": valor})


def test_valor_no_limite_da_precisao(dados_evento):
    evento = EventoCreate(**{**dados_evento, "valor": "9999999999.99"})

    assert evento.valor == Decimal("9999999999.99")


@pytest.mark.parametrize("campo, valor", [
    ("data", "2026-02-30"),
    ("inicio", "25:00"),
    ("termino", "horario invalido"),
    ("data_limite_pagamento", "2026-13-01"),
])
def test_data_ou_horario_invalido(dados_evento, campo, valor):
    with pytest.raises(ValidationError):
        EventoCreate(**{**dados_evento, campo: valor})


@pytest.mark.parametrize("campo", ["inicio", "termino"])
@pytest.mark.parametrize("valor", ["09:00:00+03:00", "09:00:00.123456"])
def test_horario_com_fuso_ou_fracao(dados_evento, campo, valor):
    with pytest.raises(ValidationError):
        EventoCreate(**{**dados_evento, campo: valor})
