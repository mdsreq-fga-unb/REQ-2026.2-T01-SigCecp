import json
import logging
from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from backend.alunos.arquivos import gravar_arquivo
from backend.alunos.models import Aluno, AlunoDocumento, AlunoTurma
from backend.alunos.schemas import (
    TAMANHO_MAXIMO_ARQUIVO,
    TIPOS_ARQUIVO_DOCUMENTO,
    TIPOS_ARQUIVO_IMAGEM,
    TIPOS_DOCUMENTO,
    TERMO_VERSAO,
    FichaAluno,
)
from backend.eventos.services import FUSO_BRASILIA
from backend.turmas.models import Turma

# Operações críticas registradas com data e usuário (RNF09)
logger = logging.getLogger("sigcecp.alunos")

# (tipo, nome do arquivo, content type, conteúdo)
Documento = tuple[str, str, str, bytes]


def agora() -> datetime:
    return datetime.now(FUSO_BRASILIA).replace(tzinfo=None, microsecond=0)


def validar_documentos(documentos: list[Documento]) -> dict[str, str]:
    """Confere tipo e tamanho dos anexos. Foto só como imagem; documentos como imagem ou PDF (RN42)."""
    erros = {}
    for tipo, _, content_type, conteudo in documentos:
        permitidos = TIPOS_ARQUIVO_IMAGEM if tipo == "foto" else TIPOS_ARQUIVO_DOCUMENTO
        if tipo not in TIPOS_DOCUMENTO:
            erros[f"doc_{tipo}"] = "Tipo de documento desconhecido."
        elif content_type not in permitidos:
            formatos = "JPG, PNG ou WEBP" if permitidos is TIPOS_ARQUIVO_IMAGEM else "JPG, PNG, WEBP ou PDF"
            erros[f"doc_{tipo}"] = f"Envie {TIPOS_DOCUMENTO[tipo].lower()} em {formatos}."
        elif len(conteudo) > TAMANHO_MAXIMO_ARQUIVO:
            erros[f"doc_{tipo}"] = "O arquivo passa de 10 MB."
    return erros


def validar_turma(db: Session, turma_id: int) -> dict[str, str]:
    turma = db.get(Turma, turma_id)
    if turma is None or not turma.ativa:
        return {"turma_id": "Escolha uma turma cadastrada."}
    return {}


def _anexar(aluno: Aluno, documentos: list[Documento], quando: datetime) -> None:
    for tipo, nome, content_type, conteudo in documentos:
        aluno.documentos.append(AlunoDocumento(
            tipo=tipo,
            nome_original=nome[:255],
            caminho=gravar_arquivo(conteudo),
            content_type=content_type,
            enviado_em=quando,
        ))


def _definir_turma(aluno: Aluno, turma_id: int, quando: datetime) -> None:
    """Troca de turma encerra o vínculo anterior e abre um novo; o histórico é preservado (DEC35)."""
    atual = aluno.vinculo_atual
    if atual is not None and atual.turma_id == turma_id:
        return
    for associacao in aluno.associacoes:
        if associacao.fim is None:
            associacao.fim = quando
    aluno.associacoes.append(AlunoTurma(turma_id=turma_id, inicio=quando))


def _aplicar_ficha(aluno: Aluno, ficha: FichaAluno) -> None:
    for campo, valor in ficha.campos.items():
        setattr(aluno, campo, valor)
    aluno.questionario = json.dumps(ficha.respostas, ensure_ascii=False)


def _salvar(db: Session, aluno: Aluno, mensagem: str) -> Aluno:
    try:
        db.commit()
        db.refresh(aluno)
        return aluno
    except Exception:
        db.rollback()
        logger.exception(mensagem)
        raise


def criar_aluno(db: Session, ficha: FichaAluno, documentos: list[Documento], usuario: str) -> Aluno:
    quando = agora()
    aluno = Aluno(
        termo_aceito_em=quando,
        termo_versao=TERMO_VERSAO,
        ativo=True,
        criado_em=quando,
    )
    _aplicar_ficha(aluno, ficha)
    _definir_turma(aluno, ficha.turma_id, quando)
    _anexar(aluno, documentos, quando)
    db.add(aluno)
    aluno = _salvar(db, aluno, "Erro ao cadastrar aluno")
    logger.info("Aluno %s cadastrado por %s em %s", aluno.id, usuario, quando.isoformat())
    return aluno


def atualizar_aluno(
    db: Session, aluno_id: int, ficha: FichaAluno, documentos: list[Documento], usuario: str
) -> Aluno:
    aluno = buscar_aluno(db, aluno_id)
    quando = agora()
    _aplicar_ficha(aluno, ficha)
    # Aluno inativo não muda de turma, a mesma regra da associação pela turma (RN01)
    if aluno.ativo and ficha.turma_id is not None:
        _definir_turma(aluno, ficha.turma_id, quando)
    _anexar(aluno, documentos, quando)
    aluno.atualizado_em = quando
    aluno = _salvar(db, aluno, "Erro ao editar aluno")
    logger.info("Aluno %s editado por %s em %s", aluno.id, usuario, quando.isoformat())
    return aluno


def inativar_aluno(db: Session, aluno_id: int, usuario: str) -> Aluno:
    """Inativa sem apagar dados nem histórico (RN01); a inativação é sempre manual (RN47)."""
    aluno = buscar_aluno(db, aluno_id)
    if not aluno.ativo:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="O aluno já está inativo.")
    quando = agora()
    aluno.ativo = False
    aluno.inativado_em = quando
    aluno = _salvar(db, aluno, "Erro ao inativar aluno")
    logger.info("Aluno %s inativado por %s em %s", aluno.id, usuario, quando.isoformat())
    return aluno


def buscar_aluno(db: Session, aluno_id: int) -> Aluno:
    aluno = db.get(Aluno, aluno_id)
    if aluno is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Aluno não encontrado")
    return aluno


def listar_alunos(db: Session, situacao: str = "todos", busca: str = "") -> list[Aluno]:
    consulta = select(Aluno).order_by(Aluno.nome)
    if busca.strip():
        consulta = consulta.where(Aluno.nome.ilike(f"%{busca.strip()}%"))
    if situacao == "ativos":
        consulta = consulta.where(Aluno.ativo.is_(True))
    elif situacao == "inativos":
        consulta = consulta.where(Aluno.ativo.is_(False))
    return list(db.scalars(consulta))


def contar_alunos(db: Session) -> dict[str, int]:
    """Contagem de ativos e inativos (RN46)."""
    linhas = db.execute(select(Aluno.ativo, func.count()).group_by(Aluno.ativo)).all()
    contagem = {bool(ativo): total for ativo, total in linhas}
    return {"ativos": contagem.get(True, 0), "inativos": contagem.get(False, 0)}


def pendencias(aluno: Aluno) -> list[str]:
    """Documentos que ainda faltam na ficha (RN39, RN41).

    O certificado só é cobrado acima da faixa branca (RN36) e o laudo só quando há problema de saúde (RN37).
    """
    # A ficha assinada comprova a assinatura presencial do responsável (RN02)
    esperados = ["ficha_assinada", "atestado", "comprovante_residencia"]
    if aluno.graduacao.strip().lower() != "branca":
        esperados.append("certificado_graduacao")
    if aluno.problema_saude:
        esperados.append("laudo")
    return [TIPOS_DOCUMENTO[tipo] for tipo in esperados if aluno.documento(tipo) is None]


def buscar_documento(db: Session, aluno_id: int, documento_id: int) -> AlunoDocumento:
    documento = db.get(AlunoDocumento, documento_id)
    if documento is None or documento.aluno_id != aluno_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Documento não encontrado")
    return documento


# ---------- Associação a partir da turma (RF06) ----------

def alunos_da_turma(db: Session, turma_id: int) -> list[Aluno]:
    """Alunos com associação aberta na turma, inclusive os inativos (DEC23)."""
    consulta = (
        select(Aluno)
        .join(AlunoTurma, AlunoTurma.aluno_id == Aluno.id)
        .where(AlunoTurma.turma_id == turma_id, AlunoTurma.fim.is_(None))
        .order_by(Aluno.nome)
    )
    return list(db.scalars(consulta))


def contar_alunos_por_turma(db: Session) -> dict[int, int]:
    """Quantidade de alunos com vínculo atual em cada turma."""
    consulta = (
        select(AlunoTurma.turma_id, func.count())
        .where(AlunoTurma.fim.is_(None))
        .group_by(AlunoTurma.turma_id)
    )
    return dict(db.execute(consulta).all())


def alunos_para_associar(db: Session, turma_id: int) -> list[Aluno]:
    ja_na_turma = {a.id for a in alunos_da_turma(db, turma_id)}
    return [a for a in listar_alunos(db, "ativos") if a.id not in ja_na_turma]


def associar_aluno_turma(db: Session, turma_id: int, aluno_id: int, usuario: str) -> Aluno:
    """Associa o aluno à turma. Como a turma é parte da ficha (RN23), um vínculo anterior é encerrado."""
    aluno = buscar_aluno(db, aluno_id)
    if not aluno.ativo:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Aluno inativo não pode ser associado.")
    atual = aluno.vinculo_atual
    if atual is not None and atual.turma_id == turma_id:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="O aluno já está nesta turma.")
    quando = agora()
    _definir_turma(aluno, turma_id, quando)
    aluno = _salvar(db, aluno, "Erro ao associar aluno à turma")
    logger.info("Aluno %s associado à turma %s por %s em %s", aluno.id, turma_id, usuario, quando.isoformat())
    return aluno
