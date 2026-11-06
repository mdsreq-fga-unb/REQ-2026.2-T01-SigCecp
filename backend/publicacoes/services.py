
import logging

from fastapi import HTTPException, UploadFile, status
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from backend.publicacoes.models import Publicacao, PublicacaoMidia
from backend.publicacoes.schemas import PublicacaoCreate
from backend.publicacoes.media import (
    salvar_midia,
    remover_midia,
    TIPOS_IMAGEM,
    TIPOS_VIDEO,
)

logger = logging.getLogger(__name__)


def criar_conteudo(
    db: Session,
    dados: PublicacaoCreate,
) -> Publicacao:
    return criar_conteudo_com_midias(db, dados)


def criar_conteudo_com_midias(
    db: Session,
    dados: PublicacaoCreate,
    imagens: list[UploadFile] | None = None,
    video: UploadFile | None = None,
) -> Publicacao:

    caminhos_salvos = []

    try:
        publicacao = Publicacao(
            titulo=dados.titulo,
            texto=dados.texto,
        )

        db.add(publicacao)
        db.flush()

        # Salvar imagens
        for imagem in imagens or []:
            caminho = salvar_midia(imagem, TIPOS_IMAGEM)

            if caminho:
                caminhos_salvos.append(caminho)

                midia = PublicacaoMidia(
                    publicacao_id=publicacao.id,
                    caminho=caminho,
                    tipo="imagem",
                    nome_original=imagem.filename or "imagem",
                )

                db.add(midia)

        # Salvar vídeo
        caminho_video = salvar_midia(video, TIPOS_VIDEO)

        if caminho_video:
            caminhos_salvos.append(caminho_video)

            midia = PublicacaoMidia(
                publicacao_id=publicacao.id,
                caminho=caminho_video,
                tipo="video",
                nome_original=video.filename or "video",
            )

            db.add(midia)

        db.commit()
        db.refresh(publicacao)

        logger.info(
            "Publicação %s criada com %s mídias",
            publicacao.id,
            len(caminhos_salvos),
        )

        return publicacao

    except ValueError as erro:
        db.rollback()

        for caminho in caminhos_salvos:
            remover_midia(caminho)

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(erro),
        )

    except Exception:
        db.rollback()

        for caminho in caminhos_salvos:
            remover_midia(caminho)

        logger.exception("Erro ao criar publicação")
        raise


def listar_conteudos(db: Session) -> list[Publicacao]:
    consulta = select(Publicacao).order_by(Publicacao.id.desc())
    return list(db.scalars(consulta).all())


def buscar_conteudo_por_id(
    db: Session,
    conteudo_id: int,
) -> Publicacao | None:
    return db.get(Publicacao, conteudo_id)


def buscar_conteudo(
    db: Session,
    conteudo_id: int,
) -> Publicacao:

    conteudo = (
        db.query(Publicacao)
        .options(selectinload(Publicacao.midias))
        .filter(Publicacao.id == conteudo_id)
        .first()
    )

    if conteudo is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Publicação não encontrada",
        )

    return conteudo


def atualizar_conteudo(
    db: Session,
    conteudo_id: int,
    dados: PublicacaoCreate,
) -> Publicacao:

    conteudo = buscar_conteudo(db, conteudo_id)

    try:
        conteudo.titulo = dados.titulo
        conteudo.texto = dados.texto

        db.commit()
        db.refresh(conteudo)

    except Exception:
        db.rollback()
        raise

    logger.info("Publicação %s editada", conteudo_id)

    return conteudo


def remover_conteudo(
    db: Session,
    conteudo_id: int,
) -> None:

    conteudo = buscar_conteudo(db, conteudo_id)

    caminhos = [
        midia.caminho
        for midia in conteudo.midias
    ]

    try:
        db.delete(conteudo)
        db.commit()

        for caminho in caminhos:
            remover_midia(caminho)

    except Exception:
        db.rollback()
        raise

    logger.info("Publicação %s removida", conteudo_id)

def atualizar_conteudo_com_midias(
    db: Session,
    conteudo_id: int,
    dados: PublicacaoCreate,
    novas_imagens: list[UploadFile] | None = None,
    novo_video: UploadFile | None = None,
    ids_midias_remover: list[int] | None = None,
    remover_video: bool = False,
) -> Publicacao:

    conteudo = buscar_conteudo(db, conteudo_id)
    ids_midias_remover = set(ids_midias_remover or [])

    caminhos_novos: list[str] = []       # para desfazer se der erro
    caminhos_antigos: list[str] = []     # só apagar do disco após o commit

    try:
        conteudo.titulo = dados.titulo
        conteudo.texto = dados.texto

        # Imagens marcadas para remoção
        for midia in list(conteudo.midias):
            if midia.tipo == "imagem" and midia.id in ids_midias_remover:
                caminhos_antigos.append(midia.caminho)
                conteudo.midias.remove(midia)
                db.delete(midia)

        # Novas imagens
        for imagem in novas_imagens or []:
            caminho = salvar_midia(imagem, TIPOS_IMAGEM)
            if caminho:
                caminhos_novos.append(caminho)
                conteudo.midias.append(
                    PublicacaoMidia(
                        caminho=caminho,
                        tipo="imagem",
                        nome_original=imagem.filename or "imagem",
                    )
                )

        # Vídeo: novo substitui; senão, checkbox remove; senão, mantém
        video_atual = next(
            (m for m in conteudo.midias if m.tipo == "video"), None
        )

        caminho_video = salvar_midia(novo_video, TIPOS_VIDEO) if novo_video else None

        if caminho_video:
            caminhos_novos.append(caminho_video)
            if video_atual:
                caminhos_antigos.append(video_atual.caminho)
                conteudo.midias.remove(video_atual)
                db.delete(video_atual)
            conteudo.midias.append(
                PublicacaoMidia(
                    caminho=caminho_video,
                    tipo="video",
                    nome_original=novo_video.filename or "video",
                )
            )
        elif remover_video and video_atual:
            caminhos_antigos.append(video_atual.caminho)
            conteudo.midias.remove(video_atual)
            db.delete(video_atual)

        db.commit()
        db.refresh(conteudo)

    except ValueError as erro:
        db.rollback()
        for caminho in caminhos_novos:
            remover_midia(caminho)
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(erro),
        )

    except Exception:
        db.rollback()
        for caminho in caminhos_novos:
            remover_midia(caminho)
        logger.exception("Erro ao editar publicação %s", conteudo_id)
        raise

    # Só depois do commit é seguro apagar os arquivos antigos
    for caminho in caminhos_antigos:
        remover_midia(caminho)

    logger.info("Publicação %s editada", conteudo_id)
    return conteudo