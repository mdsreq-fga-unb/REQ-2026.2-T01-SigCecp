import pytest
from pydantic import ValidationError

from backend.publicacoes.schemas import PublicacaoCreate


def test_publicacao_valida_com_titulo_e_texto():
    dados = PublicacaoCreate(titulo="Aula aberta", texto="Venha conhecer o CECP.")

    assert dados.titulo == "Aula aberta"
    assert dados.texto == "Venha conhecer o CECP."


def test_texto_e_opcional():
    assert PublicacaoCreate(titulo="Aula aberta").texto is None
    assert PublicacaoCreate(titulo="Aula aberta", texto=None).texto is None


def test_titulo_e_obrigatorio():
    with pytest.raises(ValidationError):
        PublicacaoCreate(texto="Só o texto")


@pytest.mark.parametrize("titulo", ["", "   ", "\n\t "])
def test_titulo_vazio_ou_so_espacos_e_rejeitado(titulo):
    with pytest.raises(ValidationError, match="O título deve ser preenchido."):
        PublicacaoCreate(titulo=titulo)


@pytest.mark.parametrize("titulo", [None, 123])
def test_titulo_com_tipo_invalido(titulo):
    with pytest.raises(ValidationError):
        PublicacaoCreate(titulo=titulo)


def test_normaliza_extremidades_sem_alterar_espacos_internos():
    dados = PublicacaoCreate(titulo="  Aula   aberta  ", texto="\n Linha 1\n\nLinha  2 \n")

    assert dados.titulo == "Aula   aberta"
    assert dados.texto == "Linha 1\n\nLinha  2"


def test_texto_so_com_espacos_vira_string_vazia():
    # A conversão para None é feita pelo router (texto or None), não pelo schema.
    assert PublicacaoCreate(titulo="Aula", texto="   ").texto == ""


def test_limite_do_titulo():
    assert len(PublicacaoCreate(titulo="a" * 200).titulo) == 200

    with pytest.raises(ValidationError):
        PublicacaoCreate(titulo="a" * 201)


def test_limite_do_texto():
    assert len(PublicacaoCreate(titulo="Aula", texto="a" * 16000).texto) == 16000

    with pytest.raises(ValidationError):
        PublicacaoCreate(titulo="Aula", texto="a" * 16001)


def test_limite_e_verificado_depois_de_remover_espacos_externos():
    dados = PublicacaoCreate(titulo=f"  {'a' * 200}  ", texto=f"\n{'b' * 16000}\n")

    assert len(dados.titulo) == 200
    assert len(dados.texto) == 16000