"""Validação e formatação dos campos da ficha do aluno (telefone, CPF, CEP, nomes e datas).

Cada função recebe o texto digitado e devolve (valor formatado, mensagem de erro ou None).
"""
import re
import unicodedata
from datetime import date

NAO_APLICAVEL = "não aplicável"

# DDDs em uso no Brasil (Anatel)
DDDS = {
    11, 12, 13, 14, 15, 16, 17, 18, 19, 21, 22, 24, 27, 28, 31, 32, 33, 34, 35, 37, 38,
    41, 42, 43, 44, 45, 46, 47, 48, 49, 51, 53, 54, 55, 61, 62, 63, 64, 65, 66, 67, 68, 69,
    71, 73, 74, 75, 77, 79, 81, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 99,
}

NOME_VALIDO = re.compile(r"^[A-Za-zÀ-ÖØ-öø-ÿ]+(?:[ '\-][A-Za-zÀ-ÖØ-öø-ÿ]+)+$")


def _sem_acento(texto: str) -> str:
    return "".join(c for c in unicodedata.normalize("NFD", texto) if unicodedata.category(c) != "Mn")


def e_nao_aplicavel(texto: str) -> bool:
    """A coordenação escreve "não aplicável" quando um dado obrigatório não existe (combinado em 10/11)."""
    return _sem_acento(texto).strip().lower() in {"nao aplicavel", "n/a", "na", "nao se aplica"}


def _digitos(texto: str) -> str:
    return re.sub(r"\D", "", texto)


def telefone(texto: str, so_celular: bool = False) -> tuple[str, str | None]:
    """DDD + 9 dígitos (celular, começando por 9) ou DDD + 8 dígitos (fixo). Aceita o 0 antes do DDD."""
    digitos = _digitos(texto)
    if len(digitos) in (11, 12) and digitos.startswith("0"):
        digitos = digitos[1:]
    if len(digitos) not in (10, 11) or int(digitos[:2]) not in DDDS:
        return texto, "Informe o telefone com DDD: (61) 99999-9999 para celular ou (61) 3333-3333 para fixo."
    numero = digitos[2:]
    if len(numero) == 9:
        if numero[0] != "9":
            return texto, "Celular tem 9 dígitos depois do DDD e começa com 9."
        return f"({digitos[:2]}) {numero[:5]}-{numero[5:]}", None
    if so_celular:
        return texto, "Informe um celular: DDD + 9 dígitos, começando com 9."
    if numero[0] not in "2345":
        return texto, "Telefone fixo tem 8 dígitos depois do DDD e começa com 2, 3, 4 ou 5."
    return f"({digitos[:2]}) {numero[:4]}-{numero[4:]}", None


def cpf(texto: str) -> tuple[str, str | None]:
    """11 dígitos, com os dois dígitos verificadores corretos."""
    digitos = _digitos(texto)
    if len(digitos) != 11:
        return texto, "O CPF tem 11 dígitos."
    if digitos == digitos[0] * 11:
        return texto, "CPF inválido."
    for posicao in (9, 10):
        soma = sum(int(digitos[i]) * (posicao + 1 - i) for i in range(posicao))
        verificador = (soma * 10) % 11 % 10
        if verificador != int(digitos[posicao]):
            return texto, "CPF inválido: confira os números."
    return f"{digitos[:3]}.{digitos[3:6]}.{digitos[6:9]}-{digitos[9:]}", None


def cep(texto: str) -> tuple[str, str | None]:
    digitos = _digitos(texto)
    if len(digitos) != 8:
        return texto, "O CEP tem 8 dígitos, como 73355-001."
    return f"{digitos[:5]}-{digitos[5:]}", None


def nome_completo(texto: str) -> tuple[str, str | None]:
    """Nome e sobrenome, só com letras, espaços, apóstrofo ou hífen."""
    limpo = " ".join(texto.split())
    if not NOME_VALIDO.match(limpo):
        return texto, "Informe o nome completo (nome e sobrenome), só com letras."
    return limpo, None


def data_nascimento(valor: date, hoje: date) -> str | None:
    if valor > hoje:
        return "A data de nascimento não pode ser no futuro."
    if valor.year < 1900:
        return "Confira o ano da data de nascimento."
    return None


def data_inicio(valor: date, nascimento: date | None, hoje: date) -> str | None:
    if nascimento and valor < nascimento:
        return "A data de início não pode ser anterior ao nascimento."
    if valor.year < 2000 or valor.year > hoje.year + 1:
        return "Confira o ano da data de início."
    return None
