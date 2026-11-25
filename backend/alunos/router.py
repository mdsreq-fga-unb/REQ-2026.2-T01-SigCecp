from urllib.parse import quote

from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import RedirectResponse, Response
from sqlalchemy.orm import Session
from starlette.datastructures import UploadFile

from backend.alunos.arquivos import ler_arquivo
from backend.alunos.schemas import (
    CAMPOS_OBRIGATORIOS,
    CAMPOS_OPCIONAIS,
    GRADUACOES,
    QUESTOES,
    SAIDAS_ALUNO,
    TIPOS_DOCUMENTO,
    TIPOS_ESCOLA,
    TURNOS,
    validar_ficha,
)
from backend.alunos.services import (
    atualizar_aluno,
    buscar_aluno,
    buscar_documento,
    contar_alunos,
    agora,
    criar_aluno,
    inativar_aluno,
    listar_alunos,
    pendencias,
    validar_documentos,
    validar_turma,
)
from backend.auth.dependencies import PROTECAO_ADMIN
from backend.config import templates
from backend.database import get_db
from backend.turmas.services import listar_turmas

# Todas as rotas deste router são administrativas e exigem login.
router = APIRouter(
    prefix="/coordenacao/alunos",
    tags=["Alunos"],
    dependencies=PROTECAO_ADMIN,
)

AVISOS = {
    "cadastrado": "Aluno cadastrado.",
    "editado": "Ficha atualizada.",
    "inativado": "Aluno inativado. O histórico foi preservado.",
}


def _usuario(request: Request) -> str:
    admin = getattr(request.state, "admin", None)
    return getattr(admin, "usuario", "coordenação")


async def _documentos_enviados(formulario) -> list[tuple[str, str, str, bytes]]:
    documentos = []
    for tipo in TIPOS_DOCUMENTO:
        arquivo = formulario.get(f"doc_{tipo}")
        if isinstance(arquivo, UploadFile) and arquivo.filename:
            documentos.append((tipo, arquivo.filename, arquivo.content_type or "", await arquivo.read()))
    return documentos


def _tela_ficha(request: Request, db: Session, modo: str, aluno=None, valores=None, erros=None, status_code=200):
    """Formulário da ficha, usado no cadastro (RF21) e na edição (RF22)."""
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/alunos/form-aluno.html",
        context={
            "modo": modo,
            "aluno": aluno,
            "valores": valores or {},
            "erros": erros or {},
            "turmas": listar_turmas(db),
            "questoes": QUESTOES,
            "tipos_documento": TIPOS_DOCUMENTO,
            "tipos_escola": TIPOS_ESCOLA,
            "graduacoes": GRADUACOES,
            "saidas": SAIDAS_ALUNO,
            "turnos": TURNOS,
        },
        status_code=status_code,
    )


def _valores_do_aluno(aluno) -> dict:
    """Valores atuais da ficha para preencher o formulário de edição."""
    valores = {
        campo: getattr(aluno, campo) or ""
        for campo in [*CAMPOS_OBRIGATORIOS, *CAMPOS_OPCIONAIS, "tipo_escola", "saida_aluno", "turno_escolar", "descricao_saude"]
    }
    valores["data_inicio"] = aluno.data_inicio.isoformat()
    valores["data_nascimento"] = aluno.data_nascimento.isoformat() if aluno.data_nascimento else ""
    valores["problema_saude"] = "sim" if aluno.problema_saude else "nao"
    valores["turma_id"] = str(aluno.vinculo_atual.turma_id) if aluno.vinculo_atual else ""
    for codigo, resposta in aluno.respostas.items():
        valores[codigo] = resposta["resposta"]
        valores[f"{codigo}_qual"] = resposta["qual"]
    return valores


def _valores_do_formulario(formulario) -> dict:
    return {chave: valor for chave, valor in formulario.items() if isinstance(valor, str)}


# ============================================================
# LISTAR ALUNOS (RF23: listagem com foto e nome, contagem RN46)
# ============================================================

@router.get("", name="lista_aluno")
def lista_alunos_pagina(request: Request, situacao: str = "todos", busca: str = "", db: Session = Depends(get_db)):
    if situacao not in ("ativos", "inativos", "todos"):
        situacao = "todos"
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/alunos/lista-aluno.html",
        context={
            "alunos": listar_alunos(db, situacao, busca),
            "situacao": situacao,
            "busca": busca.strip(),
            "contagem": contar_alunos(db),
        },
    )


# ============================================================
# CADASTRAR ALUNO (RF21)
# ============================================================

@router.get("/novo", name="cadastrar_aluno")
def cadastrar_aluno(request: Request, db: Session = Depends(get_db)):
    return _tela_ficha(request, db, "cadastrar", valores={"tipo_escola": "publica"})


@router.post("/novo", name="salvar_aluno")
async def salvar_aluno(request: Request, db: Session = Depends(get_db)):
    formulario = await request.form()
    ficha, erros = validar_ficha(formulario, exigir_termo=True)
    documentos = await _documentos_enviados(formulario)
    erros |= validar_documentos(documentos)
    if ficha:
        erros |= validar_turma(db, ficha.turma_id)
    if erros:
        return _tela_ficha(request, db, "cadastrar", valores=_valores_do_formulario(formulario), erros=erros, status_code=422)

    aluno = criar_aluno(db, ficha, documentos, _usuario(request))
    return RedirectResponse(
        str(request.url_for("ficha_aluno", aluno_id=aluno.id)) + "?aviso=cadastrado",
        status_code=303,
    )


# ============================================================
# CONSULTAR FICHA (RF23)
# ============================================================

@router.get("/{aluno_id}", name="ficha_aluno")
def ficha_aluno(aluno_id: int, request: Request, db: Session = Depends(get_db)):
    aluno = buscar_aluno(db, aluno_id)
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/alunos/ficha-aluno.html",
        context={
            "aluno": aluno,
            "pendencias": pendencias(aluno),
            "questoes": QUESTOES,
            "tipos_documento": TIPOS_DOCUMENTO,
            "tipos_escola": TIPOS_ESCOLA,
            "aviso": AVISOS.get(request.query_params.get("aviso", "")),
            "impressa_em": agora(),
        },
    )


def _content_disposition(disposicao: str, nome: str) -> str:
    """Cabeçalho aceito para qualquer nome de arquivo (RFC 6266/5987).

    Os cabeçalhos HTTP só aceitam Latin-1; nomes com acentos, travessão ou emoji vão em ``filename*``,
    com um ``filename`` ASCII de reserva para navegadores antigos.
    """
    reserva = "".join(c if c.isascii() and c.isprintable() and c not in '"\\' else "_" for c in nome) or "documento"
    return f"{disposicao}; filename=\"{reserva}\"; filename*=UTF-8''{quote(nome, safe='')}"


@router.get("/{aluno_id}/documentos/{documento_id}", name="documento_aluno")
def documento_aluno(
    aluno_id: int, documento_id: int, request: Request, baixar: bool = False, db: Session = Depends(get_db)
):
    """Entrega o documento decifrado, só para a coordenação autenticada (RNF11, RNF12)."""
    documento = buscar_documento(db, aluno_id, documento_id)
    disposicao = "attachment" if baixar else "inline"
    disposicao = _content_disposition(disposicao, documento.nome_original)
    try:
        conteudo = ler_arquivo(documento.caminho)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Arquivo do documento não encontrado") from None
    return Response(
        content=conteudo,
        media_type=documento.content_type,
        headers={
            "Content-Disposition": disposicao,
            "Cache-Control": "private, no-store",
            "X-Content-Type-Options": "nosniff",
        },
    )


# ============================================================
# EDITAR FICHA (RF22; troca ou retirada de turma pela DEC35)
# ============================================================

@router.get("/{aluno_id}/editar", name="editar_aluno")
def editar_aluno(aluno_id: int, request: Request, db: Session = Depends(get_db)):
    aluno = buscar_aluno(db, aluno_id)
    return _tela_ficha(request, db, "editar", aluno=aluno, valores=_valores_do_aluno(aluno))


@router.post("/{aluno_id}/editar", name="salvar_edicao_aluno")
async def salvar_edicao_aluno(aluno_id: int, request: Request, db: Session = Depends(get_db)):
    aluno = buscar_aluno(db, aluno_id)
    formulario = await request.form()
    # A edição mantém as regras de obrigatoriedade do cadastro (RN43); o termo já foi aceito no cadastro.
    ficha, erros = validar_ficha(formulario, exigir_termo=False, exigir_turma=aluno.ativo)
    documentos = await _documentos_enviados(formulario)
    erros |= validar_documentos(documentos)
    if ficha and ficha.turma_id is not None:
        atual = aluno.vinculo_atual.turma_id if aluno.vinculo_atual else None
        if not aluno.ativo and ficha.turma_id != atual:
            # Mesma regra da associação pela turma: aluno inativo não muda de turma (RN01)
            erros["turma_id"] = "Aluno inativo não pode mudar de turma."
        else:
            erros |= validar_turma(db, ficha.turma_id)
    if erros:
        return _tela_ficha(
            request, db, "editar", aluno=aluno, valores=_valores_do_formulario(formulario), erros=erros, status_code=422
        )

    atualizar_aluno(db, aluno_id, ficha, documentos, _usuario(request))
    return RedirectResponse(
        str(request.url_for("ficha_aluno", aluno_id=aluno_id)) + "?aviso=editado",
        status_code=303,
    )


# ============================================================
# INATIVAR ALUNO (RF24)
# ============================================================

@router.get("/{aluno_id}/inativar", name="confirmar_inativacao_aluno")
def confirmar_inativacao_aluno(aluno_id: int, request: Request, db: Session = Depends(get_db)):
    """Exibe a confirmação (RN48). Não inativa neste GET."""
    aluno = buscar_aluno(db, aluno_id)
    return templates.TemplateResponse(
        request=request,
        name="coordenacao/alunos/inativar-aluno.html",
        context={"aluno": aluno},
    )


@router.post("/{aluno_id}/inativar", name="salvar_inativacao_aluno")
def salvar_inativacao_aluno(aluno_id: int, request: Request, db: Session = Depends(get_db)):
    inativar_aluno(db, aluno_id, _usuario(request))
    return RedirectResponse(
        str(request.url_for("ficha_aluno", aluno_id=aluno_id)) + "?aviso=inativado",
        status_code=303,
    )
