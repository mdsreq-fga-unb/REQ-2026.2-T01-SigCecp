"""Rotas de conteúdo institucional: coordenação (/coordenacao/conteudo) e páginas públicas."""
from datetime import datetime

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from backend.database import Base, get_db
from backend.main import app
from backend.publicacoes.models import Publicacao, PublicacaoMidia

BASE = "/coordenacao/conteudo"


@pytest.fixture
def ambiente(tmp_path, pasta_midias):
    engine = create_engine(
        f"sqlite:///{(tmp_path / 'conteudo.db').as_posix()}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    sessoes = sessionmaker(bind=engine, autoflush=False)

    def sessao_temporaria():
        with sessoes() as db:
            yield db

    app.dependency_overrides[get_db] = sessao_temporaria
    try:
        with TestClient(app, follow_redirects=False) as cliente:
            yield cliente, sessoes, pasta_midias
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


@pytest.fixture
def cliente(ambiente):
    return ambiente[0]


@pytest.fixture
def sessoes(ambiente):
    return ambiente[1]


@pytest.fixture
def pasta(ambiente):
    return ambiente[2]


def criar(sessoes, titulo="Aula aberta", texto=None, midias=(), criada_em=None):
    """Cria uma publicação direto no banco. `midias`: tuplas (tipo, caminho, nome)."""
    with sessoes() as db:
        publicacao = Publicacao(titulo=titulo, texto=texto)
        if criada_em:
            publicacao.criada_em = criada_em
        for tipo, caminho, nome in midias:
            publicacao.midias.append(
                PublicacaoMidia(caminho=caminho, tipo=tipo, nome_original=nome)
            )
        db.add(publicacao)
        db.commit()
        return publicacao.id


def ler(sessoes, publicacao_id):
    with sessoes() as db:
        publicacao = db.get(Publicacao, publicacao_id)
        if publicacao is None:
            return None
        return {
            "titulo": publicacao.titulo,
            "texto": publicacao.texto,
            "midias": sorted((m.tipo, m.caminho) for m in publicacao.midias),
        }


def total_publicacoes(sessoes):
    with sessoes() as db:
        return db.query(Publicacao).count()


def visivel(resposta):
    """Texto da página com espaços e quebras de linha normalizados."""
    return " ".join(resposta.text.split())


def arquivos(pasta):
    destino = pasta / "publicacoes"
    return sorted(p.name for p in destino.iterdir()) if destino.exists() else []


def gravar_arquivo(pasta, nome="existente.png"):
    destino = pasta / "publicacoes"
    destino.mkdir(parents=True, exist_ok=True)
    (destino / nome).write_bytes(b"x")
    return f"publicacoes/{nome}"


PNG = ("imagem", ("foto.png", b"png-bytes", "image/png"))
MP4 = ("video", ("clipe.mp4", b"mp4-bytes", "video/mp4"))


# ============================================================
# Coordenação: lista
# ============================================================
def test_lista_vazia(cliente):
    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert "Nenhum conteúdo publicado" in resposta.text
    assert "Publicados (0)" in visivel(resposta)


def test_lista_exibe_publicacoes_da_mais_nova_para_a_mais_antiga(cliente, sessoes):
    criar(sessoes, "Primeira publicação")
    criar(sessoes, "Segunda publicação")

    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert resposta.text.index("Segunda publicação") < resposta.text.index("Primeira publicação")
    assert "Publicados (2)" in visivel(resposta)
    assert "2 conteúdos publicados" in visivel(resposta)


def test_lista_com_uma_publicacao_usa_singular(cliente, sessoes):
    criar(sessoes, "Única")

    assert "1 conteúdo publicado" in visivel(cliente.get(BASE))


def test_lista_mostra_texto_ou_aviso_de_publicacao_sem_descricao(cliente, sessoes):
    criar(sessoes, "Com texto", texto="Descrição visível")
    criar(sessoes, "Sem texto", texto=None)

    resposta = cliente.get(BASE)

    assert "Descrição visível" in resposta.text
    assert "Publicação sem descrição." in resposta.text


def test_lista_resume_a_quantidade_de_midias(cliente, sessoes):
    criar(sessoes, "Sem mídia")
    criar(sessoes, "Só imagens", midias=[
        ("imagem", "publicacoes/a.png", "a.png"), ("imagem", "publicacoes/b.png", "b.png"),
    ])
    criar(sessoes, "Imagem e vídeo", midias=[
        ("imagem", "publicacoes/c.png", "c.png"), ("video", "publicacoes/d.mp4", "d.mp4"),
    ])

    texto = visivel(cliente.get(BASE))

    assert "Nenhuma mídia" in texto
    assert "2 imagens" in texto
    assert "1 imagem e 1 vídeo" in texto


def test_lista_mostra_data_e_links_de_acao(cliente, sessoes):
    publicacao_id = criar(sessoes, "Com data", criada_em=datetime(2026, 3, 5, 10, 0))

    resposta = cliente.get(BASE)

    assert "05/03/2026" in resposta.text
    assert f"{BASE}/{publicacao_id}/editar" in resposta.text
    assert f"{BASE}/{publicacao_id}/remover" in resposta.text


# ============================================================
# Coordenação: publicar
# ============================================================
def test_formulario_de_publicacao(cliente):
    assert cliente.get(f"{BASE}/novo").status_code == 200


def test_publicar_salva_e_redireciona_para_a_lista(cliente, sessoes):
    resposta = cliente.post(f"{BASE}/novo", data={"titulo": "Nova", "texto": "Corpo do texto"})

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith(BASE)
    with sessoes() as db:
        publicacao = db.query(Publicacao).one()
        assert (publicacao.titulo, publicacao.texto) == ("Nova", "Corpo do texto")
        assert publicacao.midias == []


def test_publicar_sem_texto_grava_ausencia(cliente, sessoes):
    cliente.post(f"{BASE}/novo", data={"titulo": "Sem texto", "texto": ""})

    with sessoes() as db:
        assert db.query(Publicacao).one().texto is None


def test_publicar_remove_espacos_externos_do_titulo(cliente, sessoes):
    cliente.post(f"{BASE}/novo", data={"titulo": "  Aula aberta  "})

    with sessoes() as db:
        assert db.query(Publicacao).one().titulo == "Aula aberta"


def test_publicar_com_imagens_e_video(cliente, sessoes, pasta):
    resposta = cliente.post(
        f"{BASE}/novo",
        data={"titulo": "Com mídias"},
        files=[PNG, ("imagem", ("outra.jpg", b"jpg", "image/jpeg")), MP4],
    )

    assert resposta.status_code == 303
    with sessoes() as db:
        publicacao = db.query(Publicacao).one()
        assert sorted(m.tipo for m in publicacao.midias) == ["imagem", "imagem", "video"]
        assert {m.nome_original for m in publicacao.midias} == {"foto.png", "outra.jpg", "clipe.mp4"}
    assert len(arquivos(pasta)) == 3


def test_publicar_sem_titulo_retorna_422(cliente, sessoes):
    resposta = cliente.post(f"{BASE}/novo", data={"texto": "Sem título"})

    assert resposta.status_code == 422
    assert total_publicacoes(sessoes) == 0


def test_publicar_com_formato_invalido_retorna_400_e_nao_grava(cliente, sessoes, pasta):
    resposta = cliente.post(
        f"{BASE}/novo",
        data={"titulo": "Com PDF"},
        files=[PNG, ("imagem", ("doc.pdf", b"pdf", "application/pdf"))],
    )

    assert resposta.status_code == 400
    assert "Formato não permitido" in resposta.json()["detail"]
    assert total_publicacoes(sessoes) == 0
    assert arquivos(pasta) == []


# ============================================================
# Coordenação: editar
# ============================================================
def test_formulario_de_edicao_vem_preenchido(cliente, sessoes):
    publicacao_id = criar(sessoes, "Título atual", texto="Texto atual")

    resposta = cliente.get(f"{BASE}/{publicacao_id}/editar")

    assert resposta.status_code == 200
    assert "Título atual" in resposta.text
    assert "Texto atual" in resposta.text


def test_formulario_de_edicao_lista_as_midias_atuais(cliente, sessoes):
    publicacao_id = criar(sessoes, "Com mídias", midias=[
        ("imagem", "publicacoes/foto.png", "foto.png"),
        ("video", "publicacoes/clipe.mp4", "clipe.mp4"),
    ])

    resposta = cliente.get(f"{BASE}/{publicacao_id}/editar")

    assert "/media/publicacoes/foto.png" in resposta.text
    assert "/media/publicacoes/clipe.mp4" in resposta.text
    assert 'name="remover_midias"' in resposta.text
    assert 'name="remover_video"' in resposta.text


def test_editar_atualiza_titulo_e_texto_e_redireciona(cliente, sessoes):
    publicacao_id = criar(sessoes, "Antes", texto="Texto antes")

    resposta = cliente.post(
        f"{BASE}/{publicacao_id}/editar", data={"titulo": "Depois", "texto": "Texto depois"},
    )

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith(BASE)
    dados = ler(sessoes, publicacao_id)
    assert (dados["titulo"], dados["texto"]) == ("Depois", "Texto depois")


def test_editar_com_texto_vazio_limpa_o_texto(cliente, sessoes):
    publicacao_id = criar(sessoes, "Antes", texto="Texto antes")

    cliente.post(f"{BASE}/{publicacao_id}/editar", data={"titulo": "Antes", "texto": ""})

    assert ler(sessoes, publicacao_id)["texto"] is None


def test_editar_so_altera_a_publicacao_indicada(cliente, sessoes):
    alvo = criar(sessoes, "Alvo")
    outra = criar(sessoes, "Outra", texto="Intacta")

    cliente.post(f"{BASE}/{alvo}/editar", data={"titulo": "Alvo editado"})

    assert ler(sessoes, outra)["titulo"] == "Outra"
    assert ler(sessoes, outra)["texto"] == "Intacta"


def test_editar_adiciona_imagem_e_substitui_video(cliente, sessoes, pasta):
    imagem = gravar_arquivo(pasta, "imagem-antiga.png")
    video = gravar_arquivo(pasta, "video-antigo.mp4")
    publicacao_id = criar(sessoes, "Com mídias", midias=[
        ("imagem", imagem, "imagem-antiga.png"), ("video", video, "video-antigo.mp4"),
    ])

    resposta = cliente.post(
        f"{BASE}/{publicacao_id}/editar",
        data={"titulo": "Com mídias"},
        files=[PNG, MP4],
    )

    assert resposta.status_code == 303
    midias = ler(sessoes, publicacao_id)["midias"]
    assert [t for t, _ in midias].count("imagem") == 2
    assert [t for t, _ in midias].count("video") == 1
    assert (imagem in [c for _, c in midias]) is True
    assert (video in [c for _, c in midias]) is False
    assert "video-antigo.mp4" not in arquivos(pasta)
    assert "imagem-antiga.png" in arquivos(pasta)


def test_editar_remove_imagem_marcada(cliente, sessoes, pasta):
    caminho = gravar_arquivo(pasta, "para-remover.png")
    mantida = gravar_arquivo(pasta, "mantida.png")
    publicacao_id = criar(sessoes, "Com imagens", midias=[
        ("imagem", caminho, "para-remover.png"), ("imagem", mantida, "mantida.png"),
    ])
    with sessoes() as db:
        id_remover = next(m.id for m in db.get(Publicacao, publicacao_id).midias
                          if m.caminho == caminho)

    cliente.post(
        f"{BASE}/{publicacao_id}/editar",
        data={"titulo": "Com imagens", "remover_midias": [id_remover]},
    )

    assert ler(sessoes, publicacao_id)["midias"] == [("imagem", mantida)]
    assert arquivos(pasta) == ["mantida.png"]


def test_editar_remove_video_pelo_checkbox(cliente, sessoes, pasta):
    video = gravar_arquivo(pasta, "clipe.mp4")
    publicacao_id = criar(sessoes, "Com vídeo", midias=[("video", video, "clipe.mp4")])

    cliente.post(
        f"{BASE}/{publicacao_id}/editar",
        data={"titulo": "Com vídeo", "remover_video": "true"},
    )

    assert ler(sessoes, publicacao_id)["midias"] == []
    assert arquivos(pasta) == []


def test_editar_sem_titulo_retorna_422_e_nao_altera(cliente, sessoes):
    publicacao_id = criar(sessoes, "Original")

    resposta = cliente.post(f"{BASE}/{publicacao_id}/editar", data={"texto": "Sem título"})

    assert resposta.status_code == 422
    assert ler(sessoes, publicacao_id)["titulo"] == "Original"


def test_editar_com_formato_invalido_retorna_400_e_preserva_a_publicacao(cliente, sessoes, pasta):
    publicacao_id = criar(sessoes, "Original", texto="Texto original")

    resposta = cliente.post(
        f"{BASE}/{publicacao_id}/editar",
        data={"titulo": "Alterado"},
        files=[("imagem", ("doc.pdf", b"pdf", "application/pdf"))],
    )

    assert resposta.status_code == 400
    assert ler(sessoes, publicacao_id)["titulo"] == "Original"
    assert arquivos(pasta) == []


def test_editar_publicacao_inexistente_retorna_404(cliente):
    assert cliente.get(f"{BASE}/999/editar").status_code == 404
    assert cliente.post(f"{BASE}/999/editar", data={"titulo": "x"}).status_code == 404


@pytest.mark.xfail(
    reason="PublicacaoCreate é instanciado dentro do endpoint: título só com espaços "
           "levanta ValidationError sem tratamento (erro 500) em vez de 422.",
)
@pytest.mark.parametrize("metodo_url", ["novo", "editar"])
def test_titulo_so_com_espacos_deveria_retornar_erro_de_validacao(cliente, sessoes, metodo_url):
    publicacao_id = criar(sessoes, "Original")
    url = f"{BASE}/novo" if metodo_url == "novo" else f"{BASE}/{publicacao_id}/editar"

    resposta = cliente.post(url, data={"titulo": "   "})

    assert resposta.status_code in (400, 422)


# ============================================================
# Coordenação: remover
# ============================================================
def test_tela_de_confirmacao_nao_remove(cliente, sessoes):
    publicacao_id = criar(sessoes, "Permanece")

    resposta = cliente.get(f"{BASE}/{publicacao_id}/remover")

    assert resposta.status_code == 200
    assert "Remover publicação?" in resposta.text
    assert ler(sessoes, publicacao_id) is not None


def test_remover_apaga_registro_midias_e_arquivos(cliente, sessoes, pasta):
    imagem = gravar_arquivo(pasta, "foto.png")
    video = gravar_arquivo(pasta, "clipe.mp4")
    publicacao_id = criar(sessoes, "Será removida", midias=[
        ("imagem", imagem, "foto.png"), ("video", video, "clipe.mp4"),
    ])

    resposta = cliente.post(f"{BASE}/{publicacao_id}/remover")

    assert resposta.status_code == 303
    assert resposta.headers["location"].rstrip("/").endswith("testserver")
    assert ler(sessoes, publicacao_id) is None
    with sessoes() as db:
        assert db.query(PublicacaoMidia).count() == 0
    assert arquivos(pasta) == []


def test_remover_preserva_as_demais_publicacoes(cliente, sessoes):
    alvo = criar(sessoes, "Alvo")
    outra = criar(sessoes, "Outra")

    cliente.post(f"{BASE}/{alvo}/remover")

    assert ler(sessoes, alvo) is None
    assert ler(sessoes, outra) is not None


def test_remover_publicacao_inexistente_retorna_404(cliente):
    assert cliente.get(f"{BASE}/999/remover").status_code == 404
    assert cliente.post(f"{BASE}/999/remover").status_code == 404


# ============================================================
# Páginas públicas
# ============================================================
def test_pagina_inicial_vazia(cliente):
    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert "Nenhuma publicação ainda." in resposta.text
    assert "0 publicações" in visivel(resposta)


def test_pagina_inicial_lista_publicacoes_com_links(cliente, sessoes):
    primeira = criar(sessoes, "Primeira publicação")
    segunda = criar(sessoes, "Segunda publicação")

    resposta = cliente.get("/")

    assert resposta.status_code == 200
    assert "2 publicações" in visivel(resposta)
    assert f"/conteudo/{primeira}" in resposta.text
    assert f"/conteudo/{segunda}" in resposta.text
    assert resposta.text.index("Segunda publicação") < resposta.text.index("Primeira publicação")
    # A mais recente vira o destaque (banner) no topo da página.
    assert resposta.text.index("banner__frase") < resposta.text.index("Primeira publicação")


def test_pagina_inicial_com_uma_publicacao_usa_singular(cliente, sessoes):
    criar(sessoes, "Única")

    assert "1 publicação" in visivel(cliente.get("/"))
    assert "1 publicações" not in visivel(cliente.get("/"))


def test_pagina_inicial_resume_textos_longos(cliente, sessoes):
    texto = " ".join(f"palavra{i}" for i in range(80))
    criar(sessoes, "Texto longo", texto=texto)

    resposta = cliente.get("/")

    assert "palavra0" in resposta.text
    assert texto not in resposta.text
    assert "palavra79" not in resposta.text
    assert "..." in resposta.text


def test_pagina_publica_nao_exibe_acoes_da_coordenacao(cliente, sessoes):
    criar(sessoes, "Publicação")

    resposta = cliente.get("/")

    assert "Editar" not in resposta.text
    assert "Remover" not in resposta.text


def test_detalhe_exibe_titulo_e_paragrafos(cliente, sessoes):
    publicacao_id = criar(
        sessoes, "Título do conteúdo", texto="Primeiro parágrafo.\n\n\nSegundo parágrafo.",
    )

    resposta = cliente.get(f"/conteudo/{publicacao_id}")

    assert resposta.status_code == 200
    assert "<h1 id=\"conteudo-titulo\" class=\"detalhe__titulo\">Título do conteúdo</h1>" in resposta.text
    assert "<p>Primeiro parágrafo.</p>" in resposta.text
    assert "<p>Segundo parágrafo.</p>" in resposta.text


def test_detalhe_sem_texto_nao_cria_bloco_de_texto(cliente, sessoes):
    publicacao_id = criar(sessoes, "Só título")

    resposta = cliente.get(f"/conteudo/{publicacao_id}")

    assert resposta.status_code == 200
    assert "detalhe__texto" not in resposta.text


def test_detalhe_exibe_imagens_e_video(cliente, sessoes):
    publicacao_id = criar(sessoes, "Com mídias", midias=[
        ("imagem", "publicacoes/foto.png", "foto.png"),
        ("video", "publicacoes/clipe.mp4", "clipe.mp4"),
    ])

    resposta = cliente.get(f"/conteudo/{publicacao_id}")

    assert "/media/publicacoes/foto.png" in resposta.text
    assert 'alt="foto.png"' in resposta.text
    assert "<video" in resposta.text
    assert "/media/publicacoes/clipe.mp4" in resposta.text


def test_detalhe_sem_midias_nao_cria_bloco_de_midias(cliente, sessoes):
    publicacao_id = criar(sessoes, "Sem mídias")

    assert "detalhe__midias" not in cliente.get(f"/conteudo/{publicacao_id}").text


def test_detalhe_de_publicacao_inexistente_retorna_404(cliente):
    resposta = cliente.get("/conteudo/999999")

    assert resposta.status_code == 404
    assert resposta.json()["detail"] == "Publicação não encontrada."


@pytest.mark.xfail(
    reason="Os templates públicos usam 'criado_em', mas o modelo define 'criada_em'; "
           "a data de publicação nunca é exibida.",
)
def test_paginas_publicas_deveriam_exibir_a_data_de_publicacao(cliente, sessoes):
    publicacao_id = criar(sessoes, "Com data", criada_em=datetime(2026, 3, 5, 10, 0))

    assert "05/03/2026" in cliente.get("/").text
    assert "5 de março de 2026" in cliente.get(f"/conteudo/{publicacao_id}").text