"""Rotas async não podem usar o banco direto no laço de eventos.

O SQLAlchemy é síncrono. Uma rota `async def` que consulta o banco bloqueia o laço do servidor;
sob carga, as conexões do pool se esgotam e o servidor inteiro trava. Rotas que usam o banco
devem ser `def` (o FastAPI as roda numa thread) ou mandar o acesso ao banco para uma thread
com `run_in_threadpool`, como as listadas em ASYNC_COM_THREAD.
"""
import inspect

from fastapi.routing import APIRoute

from backend.database import get_db
from backend.main import app

# Rotas async que precisam de `await request.form()` e levam o banco para uma thread.
ASYNC_COM_THREAD = {"salvar_aluno", "salvar_edicao_aluno"}


def _todas_as_rotas(rotas):
    """Percorre também os routers incluídos (o FastAPI os guarda dentro de outro objeto)."""
    for rota in rotas:
        if isinstance(rota, APIRoute):
            yield rota
        elif hasattr(rota, "original_router"):
            yield from _todas_as_rotas(rota.original_router.routes)
        elif hasattr(rota, "routes"):
            yield from _todas_as_rotas(rota.routes)


def _usa_get_db(dependant) -> bool:
    return any(d.call is get_db or _usa_get_db(d) for d in dependant.dependencies)


def test_percorre_as_rotas_dos_routers_incluidos():
    nomes = {rota.name for rota in _todas_as_rotas(app.routes)}
    assert {"modulo_conteudo_publico", "lista_evento", "lista_conteudo", "salvar_aluno"} <= nomes


def test_rotas_async_nao_usam_o_banco_no_laco_de_eventos():
    problemas = [
        rota.name
        for rota in _todas_as_rotas(app.routes)
        if inspect.iscoroutinefunction(rota.endpoint)
        and _usa_get_db(rota.dependant)
        and rota.name not in ASYNC_COM_THREAD
    ]
    assert problemas == []
