"""Mídias dos eventos (imagem e vídeo): funções de arquivo, serviços e rotas da coordenação."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from backend.database import Base, get_db
from backend.eventos.media import TIPOS_IMAGEM, TIPOS_VIDEO, remover_midia, salvar_midia
from backend.eventos.models import Evento
from backend.eventos.schemas import EventoCreate
from backend.eventos.services import atualizar_evento, criar_evento
from backend.main import app

BASE = "/coordenacao/eventos"


@pytest.fixture(autouse=True)
def diretorio_de_trabalho_temporario(tmp_path, monkeypatch):
    # Os caminhos de mídia dos eventos são relativos ao diretório atual.
    monkeypatch.chdir(tmp_path)


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


def arquivos(tmp_path):
    pasta = tmp_path / "backend" / "media" / "eventos"
    return sorted(p.name for p in pasta.iterdir()) if pasta.exists() else []


def caminho_em_disco(tmp_path, caminho):
    return tmp_path / "backend" / "media" / caminho


def falhar(*args, **kwargs):
    raise RuntimeError("falha simulada")


def evento_com_midias(db, dados_evento, novo_upload, imagem=True, video=True):
    return criar_evento(
        db,
        EventoCreate(**dados_evento),
        imagem=novo_upload("capa.png") if imagem else None,
        video=novo_upload("clipe.mp4", "video/mp4") if video else None,
    )


# ---------- salvar_midia / remover_midia ----------
def test_tipos_permitidos():
    assert TIPOS_IMAGEM == {"image/jpeg", "image/png", "image/webp"}
    assert TIPOS_VIDEO == {"video/mp4", "video/webm", "video/ogg", "video/quicktime"}


def test_sem_arquivo_ou_sem_nome_nada_e_salvo(tmp_path, novo_upload):
    assert salvar_midia(None, TIPOS_IMAGEM) is None
    assert salvar_midia(novo_upload(nome=""), TIPOS_IMAGEM) is None
    assert arquivos(tmp_path) == []


def test_formato_nao_permitido(tmp_path, novo_upload):
    with pytest.raises(ValueError, match="Formato de arquivo não permitido."):
        salvar_midia(novo_upload("doc.pdf", "application/pdf"), TIPOS_IMAGEM)

    assert arquivos(tmp_path) == []


def test_salva_com_nome_unico_e_extensao_minuscula(tmp_path, novo_upload):
    primeiro = salvar_midia(novo_upload("FOTO.PNG", conteudo=b"abc"), TIPOS_IMAGEM)
    segundo = salvar_midia(novo_upload("FOTO.PNG"), TIPOS_IMAGEM)

    assert primeiro.startswith("eventos/") and primeiro.endswith(".png")
    assert primeiro != segundo
    assert caminho_em_disco(tmp_path, primeiro).read_bytes() == b"abc"
    assert len(arquivos(tmp_path)) == 2


def test_remover_midia(tmp_path, novo_upload):
    caminho = salvar_midia(novo_upload(), TIPOS_IMAGEM)

    remover_midia(caminho)

    assert arquivos(tmp_path) == []


@pytest.mark.parametrize("caminho", [None, "", "eventos/nao-existe.png"])
def test_remover_midia_sem_efeito(caminho):
    remover_midia(caminho)


# ---------- criar_evento ----------
def test_criar_evento_com_imagem_e_video(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)

    assert evento.imagem.startswith("eventos/") and evento.video.startswith("eventos/")
    assert caminho_em_disco(tmp_path, evento.imagem).is_file()
    assert caminho_em_disco(tmp_path, evento.video).is_file()


def test_criar_evento_sem_midias(db, tmp_path, dados_evento):
    evento = criar_evento(db, EventoCreate(**dados_evento))

    assert evento.imagem is None and evento.video is None
    assert arquivos(tmp_path) == []


def test_imagem_invalida_nao_cria_evento_nem_arquivo(db, tmp_path, dados_evento, novo_upload):
    with pytest.raises(ValueError):
        criar_evento(db, EventoCreate(**dados_evento),
                     imagem=novo_upload("a.pdf", "application/pdf"))

    assert db.query(Evento).count() == 0
    assert arquivos(tmp_path) == []


def test_falha_no_commit_remove_arquivos_gravados(
    db, tmp_path, dados_evento, novo_upload, monkeypatch,
):
    with monkeypatch.context() as m:
        m.setattr(db, "commit", falhar)
        with pytest.raises(RuntimeError):
            evento_com_midias(db, dados_evento, novo_upload)

    assert db.query(Evento).count() == 0
    assert arquivos(tmp_path) == []


@pytest.mark.xfail(
    reason="criar_evento só registra os caminhos depois de salvar imagem e vídeo; "
           "se o vídeo for inválido, a imagem já gravada fica órfã no disco.",
)
def test_video_invalido_deveria_desfazer_a_imagem_ja_gravada(
    db, tmp_path, dados_evento, novo_upload,
):
    with pytest.raises(ValueError):
        criar_evento(
            db, EventoCreate(**dados_evento),
            imagem=novo_upload("capa.png"),
            video=novo_upload("clipe.pdf", "application/pdf"),
        )

    assert arquivos(tmp_path) == []


# ---------- atualizar_evento ----------
def test_nova_imagem_substitui_a_anterior(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)
    antiga, video = evento.imagem, evento.video

    atualizar_evento(db, evento.id, EventoCreate(**dados_evento), imagem=novo_upload("nova.png"))

    assert evento.imagem != antiga
    assert caminho_em_disco(tmp_path, evento.imagem).is_file()
    assert not caminho_em_disco(tmp_path, antiga).exists()
    assert evento.video == video and caminho_em_disco(tmp_path, video).is_file()


def test_novo_video_substitui_o_anterior(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)
    antigo = evento.video

    atualizar_evento(db, evento.id, EventoCreate(**dados_evento),
                     video=novo_upload("novo.webm", "video/webm"))

    assert evento.video != antigo
    assert not caminho_em_disco(tmp_path, antigo).exists()
    assert len(arquivos(tmp_path)) == 2


def test_edicao_sem_arquivos_preserva_as_midias(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)
    antes = arquivos(tmp_path)

    atualizar_evento(db, evento.id, EventoCreate(**{**dados_evento, "titulo": "Novo título"}))

    assert evento.titulo == "Novo título"
    assert evento.imagem and evento.video
    assert arquivos(tmp_path) == antes


def test_upload_sem_nome_na_edicao_e_ignorado(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)
    antes = arquivos(tmp_path)

    atualizar_evento(db, evento.id, EventoCreate(**dados_evento),
                     imagem=novo_upload(nome=""), video=novo_upload(nome=""))

    assert arquivos(tmp_path) == antes


def test_remover_imagem_e_video_pelas_opcoes(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)

    atualizar_evento(db, evento.id, EventoCreate(**dados_evento),
                     remover_imagem=True, remover_video=True)

    assert evento.imagem is None and evento.video is None
    assert arquivos(tmp_path) == []


def test_remover_sem_midia_nao_faz_nada(db, tmp_path, dados_evento):
    evento = criar_evento(db, EventoCreate(**dados_evento))

    atualizar_evento(db, evento.id, EventoCreate(**dados_evento),
                     remover_imagem=True, remover_video=True)

    assert evento.imagem is None and evento.video is None


def test_nova_midia_tem_prioridade_sobre_remover(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)

    atualizar_evento(db, evento.id, EventoCreate(**dados_evento),
                     imagem=novo_upload("nova.png"), remover_imagem=True)

    assert evento.imagem is not None
    assert caminho_em_disco(tmp_path, evento.imagem).is_file()


def test_formato_invalido_na_edicao_preserva_tudo(db, tmp_path, dados_evento, novo_upload):
    evento = evento_com_midias(db, dados_evento, novo_upload)
    evento_id, antes = evento.id, arquivos(tmp_path)

    with pytest.raises(ValueError):
        atualizar_evento(
            db, evento_id, EventoCreate(**{**dados_evento, "titulo": "Alterado"}),
            imagem=novo_upload("nova.png"),
            video=novo_upload("v.pdf", "application/pdf"),
        )

    db.expire_all()
    assert db.get(Evento, evento_id).titulo == dados_evento["titulo"]
    assert arquivos(tmp_path) == antes  # a imagem nova foi desfeita


def test_falha_no_commit_da_edicao_preserva_antigos_e_remove_novos(
    db, tmp_path, dados_evento, novo_upload, monkeypatch,
):
    evento = evento_com_midias(db, dados_evento, novo_upload)
    evento_id, antes = evento.id, arquivos(tmp_path)

    with monkeypatch.context() as m:
        m.setattr(db, "commit", falhar)
        with pytest.raises(RuntimeError):
            atualizar_evento(db, evento_id, EventoCreate(**dados_evento),
                             imagem=novo_upload("nova.png"),
                             video=novo_upload("novo.mp4", "video/mp4"))

    assert arquivos(tmp_path) == antes


# ---------- rotas da coordenação ----------
@pytest.fixture
def ambiente(tmp_path):
    engine = create_engine(
        f"sqlite:///{(tmp_path / 'eventos-rotas.db').as_posix()}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    sessoes = sessionmaker(bind=engine, autoflush=False)

    def sessao_temporaria():
        with sessoes() as sessao:
            yield sessao

    app.dependency_overrides[get_db] = sessao_temporaria
    try:
        with TestClient(app, follow_redirects=False) as cliente:
            yield cliente, sessoes
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def unico_evento(sessoes):
    with sessoes() as sessao:
        evento = sessao.query(Evento).one()
        return {"titulo": evento.titulo, "imagem": evento.imagem, "video": evento.video}


def test_lista_vazia(ambiente):
    cliente, _ = ambiente

    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert "Nenhum evento publicado ainda." in resposta.text
    assert "0 eventos publicados" in " ".join(resposta.text.split())


def test_lista_exibe_eventos_do_mais_novo_para_o_mais_antigo(ambiente, dados_evento):
    cliente, sessoes = ambiente
    with sessoes() as sessao:
        criar_evento(sessao, EventoCreate(**{**dados_evento, "titulo": "Evento de novembro"}))
        criar_evento(sessao, EventoCreate(**{
            **dados_evento, "titulo": "Evento de dezembro", "data": "2026-12-10",
        }))

    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert resposta.text.index("Evento de dezembro") < resposta.text.index("Evento de novembro")
    assert "2 eventos publicados" in " ".join(resposta.text.split())
    assert "10/12/2026" in resposta.text


def test_formulario_de_publicacao(ambiente):
    cliente, _ = ambiente

    assert cliente.get(f"{BASE}/novo").status_code == 200


def test_publicar_evento_redireciona_para_a_pagina_publica(ambiente, dados_evento):
    cliente, sessoes = ambiente

    resposta = cliente.post(f"{BASE}/novo", data=dados_evento)

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith("/eventos")
    assert unico_evento(sessoes)["titulo"] == "Festival CECP"


def test_publicar_evento_com_midias(ambiente, tmp_path, dados_evento):
    cliente, sessoes = ambiente

    resposta = cliente.post(
        f"{BASE}/novo", data=dados_evento,
        files=[("imagem", ("capa.png", b"png", "image/png")),
               ("video", ("clipe.mp4", b"mp4", "video/mp4"))],
    )

    assert resposta.status_code == 303
    evento = unico_evento(sessoes)
    assert caminho_em_disco(tmp_path, evento["imagem"]).is_file()
    assert caminho_em_disco(tmp_path, evento["video"]).is_file()


@pytest.mark.parametrize("campo", ["titulo", "data", "inicio", "termino", "pesagem"])
def test_publicar_sem_campo_obrigatorio_retorna_422(ambiente, dados_evento, campo):
    cliente, sessoes = ambiente
    dados = {k: v for k, v in dados_evento.items() if k != campo}

    resposta = cliente.post(f"{BASE}/novo", data=dados)

    assert resposta.status_code == 422
    with sessoes() as sessao:
        assert sessao.query(Evento).count() == 0


def test_publicar_evento_cobrado_sem_valor_retorna_422(ambiente, dados_evento):
    cliente, _ = ambiente

    resposta = cliente.post(f"{BASE}/novo", data={**dados_evento, "cobrado": True})

    assert resposta.status_code == 422


def test_editar_substitui_imagem_pela_rota(ambiente, tmp_path, dados_evento, novo_upload):
    cliente, sessoes = ambiente
    with sessoes() as sessao:
        evento = evento_com_midias(sessao, dados_evento, novo_upload, video=False)
        evento_id, antiga = evento.id, evento.imagem

    resposta = cliente.post(
        f"{BASE}/{evento_id}/editar", data=dados_evento,
        files=[("imagem", ("nova.png", b"novo", "image/png"))],
    )

    assert resposta.status_code == 303
    nova = unico_evento(sessoes)["imagem"]
    assert nova != antiga
    assert caminho_em_disco(tmp_path, nova).is_file()
    assert not caminho_em_disco(tmp_path, antiga).exists()


def test_editar_remove_midias_pelas_opcoes(ambiente, tmp_path, dados_evento, novo_upload):
    cliente, sessoes = ambiente
    with sessoes() as sessao:
        evento_id = evento_com_midias(sessao, dados_evento, novo_upload).id

    resposta = cliente.post(
        f"{BASE}/{evento_id}/editar",
        data={**dados_evento, "remover_imagem": "true", "remover_video": "true"},
    )

    assert resposta.status_code == 303
    evento = unico_evento(sessoes)
    assert evento["imagem"] is None and evento["video"] is None
    assert arquivos(tmp_path) == []


def test_lista_de_coordenacao_tem_acoes_de_cada_evento(ambiente, dados_evento):
    cliente, sessoes = ambiente
    with sessoes() as sessao:
        evento_id = criar_evento(sessao, EventoCreate(**dados_evento)).id

    resposta = cliente.get(BASE)

    assert f"{BASE}/{evento_id}/editar" in resposta.text
    assert f"{BASE}/{evento_id}/remover" in resposta.text


@pytest.mark.xfail(
    reason="O router de eventos não converte o ValueError de formato inválido em "
           "resposta HTTP (publicações devolve 400); o erro vira 500.",
)
def test_publicar_com_formato_invalido_deveria_retornar_erro_de_cliente(ambiente, dados_evento):
    cliente, _ = ambiente

    resposta = cliente.post(
        f"{BASE}/novo", data=dados_evento,
        files=[("imagem", ("doc.pdf", b"pdf", "application/pdf"))],
    )

    assert resposta.status_code in (400, 422)