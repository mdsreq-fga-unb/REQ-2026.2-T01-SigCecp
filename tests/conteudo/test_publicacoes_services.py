import pytest
from fastapi import HTTPException
from sqlalchemy import create_engine, func, select
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.database import Base
from backend.publicacoes.models import Publicacao, PublicacaoMidia
from backend.publicacoes.schemas import PublicacaoCreate
from backend.publicacoes.services import (
    atualizar_conteudo,
    atualizar_conteudo_com_midias,
    buscar_conteudo,
    buscar_conteudo_por_id,
    criar_conteudo,
    criar_conteudo_com_midias,
    listar_conteudos,
    remover_conteudo,
)


@pytest.fixture
def db():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool,
    )
    Base.metadata.create_all(engine)
    sessao = sessionmaker(bind=engine, autoflush=False)()
    yield sessao
    sessao.close()
    engine.dispose()


def dados(titulo="Título", texto="Texto"):
    return PublicacaoCreate(titulo=titulo, texto=texto)


def total(db, modelo):
    return db.scalar(select(func.count()).select_from(modelo))


def arquivos_em_disco(pasta_midias):
    pasta = pasta_midias / "publicacoes"
    return sorted(p.name for p in pasta.iterdir()) if pasta.exists() else []


def falhar(*args, **kwargs):
    raise RuntimeError("falha simulada")


@pytest.fixture
def publicacao_completa(db, pasta_midias, novo_upload):
    """Publicação com 2 imagens e 1 vídeo já gravados no banco e no disco."""
    return criar_conteudo_com_midias(
        db,
        dados("Original", "Texto original"),
        imagens=[novo_upload("a.png"), novo_upload("b.jpg", "image/jpeg")],
        video=novo_upload("v.mp4", "video/mp4"),
    )


def midias_por_tipo(publicacao, tipo):
    return [m for m in publicacao.midias if m.tipo == tipo]


# ---------- criar ----------
def test_criar_conteudo_sem_midias(db, pasta_midias):
    publicacao = criar_conteudo(db, dados("Aula aberta", "Venha conhecer."))

    assert publicacao.id is not None
    assert publicacao.titulo == "Aula aberta"
    assert publicacao.texto == "Venha conhecer."
    assert publicacao.criada_em is not None
    assert publicacao.midias == []
    assert total(db, Publicacao) == 1
    assert arquivos_em_disco(pasta_midias) == []


def test_criar_conteudo_com_texto_ausente(db, pasta_midias):
    publicacao = criar_conteudo(db, PublicacaoCreate(titulo="Só título"))

    assert publicacao.texto is None


def test_criar_com_imagens_e_video(db, pasta_midias, novo_upload):
    publicacao = criar_conteudo_com_midias(
        db,
        dados(),
        imagens=[novo_upload("a.png", conteudo=b"AAA"), novo_upload("b.JPG", "image/jpeg")],
        video=novo_upload("v.mp4", "video/mp4"),
    )

    assert sorted(m.tipo for m in publicacao.midias) == ["imagem", "imagem", "video"]
    assert {m.nome_original for m in publicacao.midias} == {"a.png", "b.JPG", "v.mp4"}
    for midia in publicacao.midias:
        assert midia.publicacao_id == publicacao.id
        assert midia.caminho.startswith("publicacoes/")
        assert (pasta_midias / midia.caminho).is_file()
    assert any(m.caminho.endswith(".jpg") for m in publicacao.midias)
    assert len(arquivos_em_disco(pasta_midias)) == 3


def test_uploads_sem_nome_sao_ignorados(db, pasta_midias, novo_upload):
    publicacao = criar_conteudo_com_midias(
        db, dados(), imagens=[novo_upload(nome="")], video=novo_upload(nome=""),
    )

    assert publicacao.midias == []
    assert arquivos_em_disco(pasta_midias) == []


def test_aceita_video_quicktime(db, pasta_midias, novo_upload):
    publicacao = criar_conteudo_com_midias(
        db, dados(), video=novo_upload("v.mov", "video/quicktime"),
    )

    assert [m.tipo for m in publicacao.midias] == ["video"]


def test_imagem_invalida_gera_400_e_nao_deixa_rastros(db, pasta_midias, novo_upload):
    with pytest.raises(HTTPException) as erro:
        criar_conteudo_com_midias(
            db,
            dados(),
            imagens=[novo_upload("ok.png"), novo_upload("doc.pdf", "application/pdf")],
        )

    assert erro.value.status_code == 400
    assert "Formato não permitido: application/pdf" in erro.value.detail
    assert total(db, Publicacao) == 0
    assert total(db, PublicacaoMidia) == 0
    assert arquivos_em_disco(pasta_midias) == []  # a primeira imagem foi desfeita

    # A sessão continua utilizável depois do rollback.
    assert criar_conteudo(db, dados("Depois do erro")).id is not None


def test_video_com_tipo_de_imagem_e_rejeitado(db, pasta_midias, novo_upload):
    with pytest.raises(HTTPException) as erro:
        criar_conteudo_com_midias(db, dados(), video=novo_upload("v.png", "image/png"))

    assert erro.value.status_code == 400
    assert total(db, Publicacao) == 0


def test_imagem_com_tipo_de_video_e_rejeitada(db, pasta_midias, novo_upload):
    with pytest.raises(HTTPException) as erro:
        criar_conteudo_com_midias(db, dados(), imagens=[novo_upload("a.mp4", "video/mp4")])

    assert erro.value.status_code == 400
    assert total(db, Publicacao) == 0


def test_video_invalido_desfaz_as_imagens_ja_gravadas(db, pasta_midias, novo_upload):
    with pytest.raises(HTTPException):
        criar_conteudo_com_midias(
            db,
            dados(),
            imagens=[novo_upload("a.png"), novo_upload("b.png")],
            video=novo_upload("v.pdf", "application/pdf"),
        )

    assert total(db, Publicacao) == 0
    assert arquivos_em_disco(pasta_midias) == []


def test_falha_inesperada_no_commit_desfaz_tudo(db, pasta_midias, novo_upload, monkeypatch):
    with monkeypatch.context() as m:
        m.setattr(db, "commit", falhar)
        with pytest.raises(RuntimeError, match="falha simulada"):
            criar_conteudo_com_midias(
                db, dados(), imagens=[novo_upload()], video=novo_upload("v.mp4", "video/mp4"),
            )

    assert total(db, Publicacao) == 0
    assert total(db, PublicacaoMidia) == 0
    assert arquivos_em_disco(pasta_midias) == []


# ---------- consultar ----------
def test_listar_conteudos_vazio(db):
    assert listar_conteudos(db) == []


def test_listar_conteudos_do_mais_novo_para_o_mais_antigo(db, pasta_midias):
    primeiro = criar_conteudo(db, dados("Primeiro")).id
    segundo = criar_conteudo(db, dados("Segundo")).id
    terceiro = criar_conteudo(db, dados("Terceiro")).id

    assert [p.id for p in listar_conteudos(db)] == [terceiro, segundo, primeiro]


def test_buscar_conteudo_por_id(db, pasta_midias):
    publicacao = criar_conteudo(db, dados("Aula aberta"))

    assert buscar_conteudo_por_id(db, publicacao.id).titulo == "Aula aberta"
    assert buscar_conteudo_por_id(db, 999) is None


def test_buscar_conteudo_inexistente_gera_404(db):
    with pytest.raises(HTTPException) as erro:
        buscar_conteudo(db, 999)

    assert erro.value.status_code == 404
    assert erro.value.detail == "Publicação não encontrada"


def test_buscar_conteudo_traz_as_midias(db, publicacao_completa):
    db.expire_all()

    encontrada = buscar_conteudo(db, publicacao_completa.id)

    assert len(encontrada.midias) == 3


# ---------- atualizar (somente texto) ----------
def test_atualizar_conteudo(db, pasta_midias):
    publicacao = criar_conteudo(db, dados("Antes", "Texto antes"))

    atualizada = atualizar_conteudo(db, publicacao.id, dados("Depois", "Texto depois"))

    assert (atualizada.titulo, atualizada.texto) == ("Depois", "Texto depois")
    db.expire_all()
    assert buscar_conteudo(db, publicacao.id).titulo == "Depois"


def test_atualizar_conteudo_pode_limpar_o_texto(db, pasta_midias):
    publicacao = criar_conteudo(db, dados("Antes", "Texto antes"))

    atualizar_conteudo(db, publicacao.id, PublicacaoCreate(titulo="Antes"))

    assert buscar_conteudo(db, publicacao.id).texto is None


def test_atualizar_conteudo_inexistente_gera_404(db):
    with pytest.raises(HTTPException) as erro:
        atualizar_conteudo(db, 999, dados())

    assert erro.value.status_code == 404


def test_atualizar_conteudo_com_falha_faz_rollback(db, pasta_midias, monkeypatch):
    publicacao = criar_conteudo(db, dados("Antes"))

    with monkeypatch.context() as m:
        m.setattr(db, "commit", falhar)
        with pytest.raises(RuntimeError):
            atualizar_conteudo(db, publicacao.id, dados("Depois"))

    db.expire_all()
    assert buscar_conteudo(db, publicacao.id).titulo == "Antes"


# ---------- remover ----------
def test_remover_conteudo_apaga_registro_midias_e_arquivos(db, pasta_midias, publicacao_completa):
    assert len(arquivos_em_disco(pasta_midias)) == 3

    remover_conteudo(db, publicacao_completa.id)

    assert total(db, Publicacao) == 0
    assert total(db, PublicacaoMidia) == 0
    assert arquivos_em_disco(pasta_midias) == []


def test_remover_conteudo_preserva_as_outras_publicacoes(db, pasta_midias, novo_upload):
    alvo = criar_conteudo_com_midias(db, dados("Alvo"), imagens=[novo_upload("a.png")])
    outra = criar_conteudo_com_midias(db, dados("Outra"), imagens=[novo_upload("b.png")])
    caminho_outra = outra.midias[0].caminho

    remover_conteudo(db, alvo.id)

    assert [p.titulo for p in listar_conteudos(db)] == ["Outra"]
    assert (pasta_midias / caminho_outra).is_file()
    assert len(arquivos_em_disco(pasta_midias)) == 1


def test_remover_conteudo_inexistente_gera_404(db):
    with pytest.raises(HTTPException) as erro:
        remover_conteudo(db, 999)

    assert erro.value.status_code == 404


def test_falha_ao_remover_preserva_registro_e_arquivos(
    db, pasta_midias, publicacao_completa, monkeypatch,
):
    with monkeypatch.context() as m:
        m.setattr(db, "commit", falhar)
        with pytest.raises(RuntimeError):
            remover_conteudo(db, publicacao_completa.id)

    assert total(db, Publicacao) == 1
    assert total(db, PublicacaoMidia) == 3
    assert len(arquivos_em_disco(pasta_midias)) == 3


# ---------- atualizar com mídias ----------
def test_edicao_sem_arquivos_novos_preserva_as_midias(db, pasta_midias, publicacao_completa):
    antes = arquivos_em_disco(pasta_midias)

    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados("Novo título", "Novo texto"),
    )

    assert (atualizada.titulo, atualizada.texto) == ("Novo título", "Novo texto")
    assert len(atualizada.midias) == 3
    assert arquivos_em_disco(pasta_midias) == antes


def test_edicao_adiciona_imagens_mantendo_as_existentes(
    db, pasta_midias, publicacao_completa, novo_upload,
):
    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(), novas_imagens=[novo_upload("nova.webp", "image/webp")],
    )

    assert len(midias_por_tipo(atualizada, "imagem")) == 3
    assert len(midias_por_tipo(atualizada, "video")) == 1
    assert any(m.nome_original == "nova.webp" for m in atualizada.midias)
    assert len(arquivos_em_disco(pasta_midias)) == 4


def test_edicao_remove_imagens_marcadas_e_apaga_os_arquivos(
    db, pasta_midias, publicacao_completa,
):
    imagens = midias_por_tipo(publicacao_completa, "imagem")
    removida, mantida = imagens[0], imagens[1]
    caminho_removido, caminho_mantido = removida.caminho, mantida.caminho

    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(), ids_midias_remover=[removida.id],
    )

    assert [m.id for m in midias_por_tipo(atualizada, "imagem")] == [mantida.id]
    assert not (pasta_midias / caminho_removido).exists()
    assert (pasta_midias / caminho_mantido).is_file()
    assert total(db, PublicacaoMidia) == 2


def test_ids_de_video_em_remover_midias_nao_removem_o_video(
    db, pasta_midias, publicacao_completa,
):
    video = midias_por_tipo(publicacao_completa, "video")[0]

    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(), ids_midias_remover=[video.id],
    )

    assert len(midias_por_tipo(atualizada, "video")) == 1
    assert (pasta_midias / video.caminho).is_file()


def test_ids_inexistentes_em_remover_midias_sao_ignorados(db, pasta_midias, publicacao_completa):
    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(), ids_midias_remover=[9999],
    )

    assert len(atualizada.midias) == 3
    assert len(arquivos_em_disco(pasta_midias)) == 3


def test_novo_video_substitui_o_anterior(db, pasta_midias, publicacao_completa, novo_upload):
    antigo = midias_por_tipo(publicacao_completa, "video")[0].caminho

    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(),
        novo_video=novo_upload("novo.webm", "video/webm"),
    )

    videos = midias_por_tipo(atualizada, "video")
    assert len(videos) == 1
    assert videos[0].nome_original == "novo.webm"
    assert not (pasta_midias / antigo).exists()
    assert (pasta_midias / videos[0].caminho).is_file()
    assert len(arquivos_em_disco(pasta_midias)) == 3


def test_novo_video_em_publicacao_que_nao_tinha(db, pasta_midias, novo_upload):
    publicacao = criar_conteudo(db, dados())

    atualizada = atualizar_conteudo_com_midias(
        db, publicacao.id, dados(), novo_video=novo_upload("v.mp4", "video/mp4"),
    )

    assert [m.tipo for m in atualizada.midias] == ["video"]
    assert len(arquivos_em_disco(pasta_midias)) == 1


def test_remover_video(db, pasta_midias, publicacao_completa):
    video = midias_por_tipo(publicacao_completa, "video")[0]
    caminho = video.caminho

    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(), remover_video=True,
    )

    assert midias_por_tipo(atualizada, "video") == []
    assert len(midias_por_tipo(atualizada, "imagem")) == 2
    assert not (pasta_midias / caminho).exists()


def test_remover_video_sem_video_nao_faz_nada(db, pasta_midias, novo_upload):
    publicacao = criar_conteudo_com_midias(db, dados(), imagens=[novo_upload()])

    atualizada = atualizar_conteudo_com_midias(db, publicacao.id, dados(), remover_video=True)

    assert [m.tipo for m in atualizada.midias] == ["imagem"]


def test_novo_video_tem_prioridade_sobre_remover_video(
    db, pasta_midias, publicacao_completa, novo_upload,
):
    atualizada = atualizar_conteudo_com_midias(
        db, publicacao_completa.id, dados(),
        novo_video=novo_upload("novo.mp4", "video/mp4"),
        remover_video=True,
    )

    videos = midias_por_tipo(atualizada, "video")
    assert [v.nome_original for v in videos] == ["novo.mp4"]


def test_edicao_com_formato_invalido_nao_altera_nada(
    db, pasta_midias, publicacao_completa, novo_upload,
):
    antes = arquivos_em_disco(pasta_midias)
    imagem_id = midias_por_tipo(publicacao_completa, "imagem")[0].id
    publicacao_id = publicacao_completa.id

    with pytest.raises(HTTPException) as erro:
        atualizar_conteudo_com_midias(
            db, publicacao_id, dados("Título alterado", "Texto alterado"),
            novas_imagens=[novo_upload("ok.png"), novo_upload("doc.pdf", "application/pdf")],
            ids_midias_remover=[imagem_id],
            remover_video=True,
        )

    assert erro.value.status_code == 400
    db.expire_all()
    original = buscar_conteudo(db, publicacao_id)
    assert (original.titulo, original.texto) == ("Original", "Texto original")
    assert len(original.midias) == 3
    assert arquivos_em_disco(pasta_midias) == antes  # nova imagem desfeita, antigas preservadas


def test_falha_inesperada_na_edicao_preserva_antigos_e_remove_novos(
    db, pasta_midias, publicacao_completa, novo_upload, monkeypatch,
):
    antes = arquivos_em_disco(pasta_midias)
    publicacao_id = publicacao_completa.id

    with monkeypatch.context() as m:
        m.setattr(db, "commit", falhar)
        with pytest.raises(RuntimeError):
            atualizar_conteudo_com_midias(
                db, publicacao_id, dados("Outro"),
                novas_imagens=[novo_upload("nova.png")],
                novo_video=novo_upload("novo.mp4", "video/mp4"),
            )

    db.expire_all()
    assert buscar_conteudo(db, publicacao_id).titulo == "Original"
    assert arquivos_em_disco(pasta_midias) == antes


def test_edicao_de_publicacao_inexistente_gera_404(db, pasta_midias):
    with pytest.raises(HTTPException) as erro:
        atualizar_conteudo_com_midias(db, 999, dados())

    assert erro.value.status_code == 404