import pytest

from backend.publicacoes import media
from backend.publicacoes.media import (
    TIPOS_IMAGEM,
    TIPOS_VIDEO,
    remover_midia,
    salvar_midia,
)


def test_tipos_permitidos():
    assert TIPOS_IMAGEM == {"image/jpeg", "image/png", "image/webp"}
    assert TIPOS_VIDEO == {"video/mp4", "video/webm", "video/ogg", "video/quicktime"}


# ---------- salvar_midia ----------
def test_sem_arquivo_ou_sem_nome_nada_e_salvo(pasta_midias, novo_upload):
    assert salvar_midia(None, TIPOS_IMAGEM) is None
    assert salvar_midia(novo_upload(nome=""), TIPOS_IMAGEM) is None
    assert not pasta_midias.exists()


def test_formato_nao_permitido_levanta_erro_e_nao_grava(pasta_midias, novo_upload):
    with pytest.raises(ValueError, match="Formato não permitido: application/pdf"):
        salvar_midia(novo_upload("doc.pdf", "application/pdf"), TIPOS_IMAGEM)

    assert not pasta_midias.exists()


def test_tipo_de_video_nao_vale_como_imagem_e_vice_versa(pasta_midias, novo_upload):
    with pytest.raises(ValueError):
        salvar_midia(novo_upload("a.mp4", "video/mp4"), TIPOS_IMAGEM)
    with pytest.raises(ValueError):
        salvar_midia(novo_upload("a.png", "image/png"), TIPOS_VIDEO)


def test_salva_arquivo_e_devolve_caminho_relativo(pasta_midias, novo_upload):
    caminho = salvar_midia(novo_upload("foto.png", conteudo=b"bytes-da-imagem"), TIPOS_IMAGEM)

    assert caminho.startswith("publicacoes/")
    assert caminho.endswith(".png")
    assert (pasta_midias / caminho).read_bytes() == b"bytes-da-imagem"


def test_cria_a_pasta_quando_ela_nao_existe(pasta_midias, novo_upload):
    assert not (pasta_midias / "publicacoes").exists()

    salvar_midia(novo_upload(), TIPOS_IMAGEM)

    assert (pasta_midias / "publicacoes").is_dir()


def test_extensao_e_normalizada_para_minusculas(pasta_midias, novo_upload):
    caminho = salvar_midia(novo_upload("FOTO.JPG", "image/jpeg"), TIPOS_IMAGEM)

    assert caminho.endswith(".jpg")


def test_nome_original_nao_e_usado_no_nome_gravado(pasta_midias, novo_upload):
    caminho = salvar_midia(novo_upload("../../segredo.png"), TIPOS_IMAGEM)

    assert "segredo" not in caminho
    assert ".." not in caminho
    assert (pasta_midias / caminho).is_file()


def test_arquivos_com_o_mesmo_nome_recebem_caminhos_diferentes(pasta_midias, novo_upload):
    primeiro = salvar_midia(novo_upload("foto.png"), TIPOS_IMAGEM)
    segundo = salvar_midia(novo_upload("foto.png"), TIPOS_IMAGEM)

    assert primeiro != segundo
    assert (pasta_midias / primeiro).is_file()
    assert (pasta_midias / segundo).is_file()


@pytest.mark.parametrize("tipo", sorted(TIPOS_VIDEO))
def test_aceita_todos_os_tipos_de_video(pasta_midias, novo_upload, tipo):
    assert salvar_midia(novo_upload("v.bin", tipo), TIPOS_VIDEO)


# ---------- remover_midia ----------
def test_remove_arquivo_existente(pasta_midias, novo_upload):
    caminho = salvar_midia(novo_upload(), TIPOS_IMAGEM)

    remover_midia(caminho)

    assert not (pasta_midias / caminho).exists()


@pytest.mark.parametrize("caminho", [None, ""])
def test_remover_sem_caminho_nao_faz_nada(pasta_midias, caminho):
    remover_midia(caminho)


def test_remover_arquivo_inexistente_nao_levanta_erro(pasta_midias):
    remover_midia("publicacoes/nao-existe.png")


def test_remover_nao_apaga_arquivos_fora_da_pasta_de_midias(pasta_midias, tmp_path):
    pasta_midias.mkdir()
    fora = tmp_path / "fora.txt"
    fora.write_text("não pode ser apagado")

    remover_midia("../fora.txt")

    assert fora.exists()


def test_remover_nao_apaga_diretorios(pasta_midias):
    (pasta_midias / "publicacoes").mkdir(parents=True)

    remover_midia("publicacoes")

    assert (pasta_midias / "publicacoes").is_dir()


def test_diretorios_padrao_ficam_em_backend_media():
    assert media.DIRETORIO_BASE.name == "media"
    assert media.DIRETORIO_BASE.parent.name == "backend"
    assert media.DIRETORIO_PUBLICACOES == media.DIRETORIO_BASE / "publicacoes"