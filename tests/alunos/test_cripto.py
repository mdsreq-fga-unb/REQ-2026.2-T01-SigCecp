"""Chave e cifra dos dados sensíveis do aluno (backend/cripto.py, RNF12)."""
import pytest

from backend import cripto


@pytest.fixture
def sem_cifra_carregada(monkeypatch):
    monkeypatch.setattr(cripto, "_fernet", None)


def test_cifrar_e_decifrar(sem_cifra_carregada):
    cifrado = cripto.cifrar(b"laudo")

    assert b"laudo" not in cifrado
    assert cripto.decifrar(cifrado) == b"laudo"


def test_producao_sem_chave_nao_sobe(sem_cifra_carregada, monkeypatch):
    monkeypatch.delenv("DADOS_CHAVE")
    monkeypatch.setenv("APP_ENV", "production")

    with pytest.raises(RuntimeError, match="DADOS_CHAVE"):
        cripto.cifrar(b"x")


def test_desenvolvimento_sem_chave_cria_e_reaproveita_a_chave(sem_cifra_carregada, monkeypatch, tmp_path):
    monkeypatch.delenv("DADOS_CHAVE")
    monkeypatch.setenv("APP_ENV", "development")
    monkeypatch.setattr(cripto, "ARQUIVO_CHAVE_DEV", tmp_path / ".chave")

    cifrado = cripto.cifrar(b"dado")
    monkeypatch.setattr(cripto, "_fernet", None)

    assert (tmp_path / ".chave").exists()
    assert cripto.decifrar(cifrado) == b"dado"
