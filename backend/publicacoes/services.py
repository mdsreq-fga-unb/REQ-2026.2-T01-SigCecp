
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
