"""Erros mostrados ao navegador como página em português, e não como JSON.

Pedidos que não aceitam HTML (API, testes) continuam recebendo o JSON padrão do FastAPI.
"""
from fastapi import Request
from fastapi.exception_handlers import http_exception_handler, request_validation_exception_handler
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException

from backend.config import templates

ROTULOS = {
    "titulo": "Título", "subtitulo": "Subtítulo", "nome": "Nome", "texto": "Texto", "data": "Data",
    "inicio": "Horário de início", "termino": "Horário de término", "local": "Local", "descricao": "Descrição",
    "alimentacao": "Alimentação", "pesagem": "Pesagem", "cobrado": "Cobrança", "valor": "Valor",
    "meio_pagamento": "Meio de pagamento", "modalidade": "Modalidade", "dias": "Dias",
    "imagem": "Imagem", "video": "Vídeo", "usuario": "Usuário", "senha": "Senha",
}

MENSAGENS = {
    "missing": "preencha este campo.",
    "string_too_long": "o texto está longo demais.",
    "string_too_short": "o texto está curto demais.",
    "too_short": "marque pelo menos uma opção.",
    "literal_error": "escolha uma das opções da lista.",
    "time_parsing": "use um horário no formato 14:30.",
    "time_type": "use um horário no formato 14:30.",
    "date_from_datetime_parsing": "use uma data no formato dia/mês/ano.",
    "date_parsing": "use uma data no formato dia/mês/ano.",
    "bool_parsing": "escolha uma das opções.",
    "decimal_parsing": "use um número, como 25,00.",
    "float_parsing": "use um número, como 25,00.",
}

TITULOS_STATUS = {
    400: "Não foi possível salvar",
    404: "Página não encontrada",
    409: "Não foi possível salvar",
    413: "Arquivo grande demais",
    422: "Não foi possível salvar",
}


def _quer_html(request: Request) -> bool:
    return "text/html" in request.headers.get("accept", "")


def _destino(request: Request) -> tuple[str, str]:
    if request.url.path.startswith("/coordenacao"):
        return "/coordenacao", "Ir para a Central da coordenação"
    return "/", "Ir para a página inicial"


def _pagina(request: Request, status: int, titulo: str, mensagem: str, problemas=None, voltar=False):
    destino, rotulo = _destino(request)
    return templates.TemplateResponse(
        request=request,
        name="erro.html",
        context={
            "titulo": titulo, "mensagem": mensagem, "problemas": problemas or [], "voltar": voltar,
            "destino": destino, "destino_rotulo": rotulo,
        },
        status_code=status,
    )


def _problema(erro: dict) -> str:
    campo = next((str(parte) for parte in reversed(erro.get("loc", [])) if isinstance(parte, str)), "")
    if campo in ("", "body"):
        # Erro do formulário como um todo (model_validator): a mensagem já diz o campo.
        return str(erro.get("msg", "")).removeprefix("Value error, ")
    rotulo = ROTULOS.get(campo, campo.replace("_", " ").capitalize() or "Um campo")
    texto = MENSAGENS.get(erro.get("type", ""))
    if texto is None:
        texto = "valor inválido. " + str(erro.get("msg", "")).removeprefix("Value error, ")
    return f"{rotulo}: {texto}"


async def tratar_validacao(request: Request, exc: RequestValidationError):
    if not _quer_html(request):
        return await request_validation_exception_handler(request, exc)
    problemas = list(dict.fromkeys(_problema(erro) for erro in exc.errors()))
    return _pagina(
        request, 422, "Não foi possível salvar",
        "Revise os campos abaixo. Ao voltar, os dados que você digitou continuam no formulário.",
        problemas, voltar=True,
    )


async def tratar_http(request: Request, exc: HTTPException):
    if not _quer_html(request) or exc.status_code < 400 or exc.status_code in (401, 405):
        return await http_exception_handler(request, exc)
    titulo = TITULOS_STATUS.get(exc.status_code, "Algo deu errado")
    mensagem = exc.detail if isinstance(exc.detail, str) else "Não foi possível concluir a ação."
    if exc.status_code == 404 and mensagem == "Not Found":
        mensagem = "O endereço não existe ou o registro foi removido."
    return _pagina(request, exc.status_code, titulo, mensagem, voltar=exc.status_code != 404)
