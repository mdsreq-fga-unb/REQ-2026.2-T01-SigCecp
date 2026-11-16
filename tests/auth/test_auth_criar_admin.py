import pytest
from sqlalchemy import select

from backend.auth import criar_admin, services
from backend.auth.models import Administrador, RefreshToken

pytestmark = pytest.mark.auth_real

SENHA = "senha-forte-123"


def _senhas(monkeypatch, *valores):
    it = iter(valores)
    monkeypatch.setattr(criar_admin.getpass, "getpass", lambda _p="": next(it))


def test_cria_admin_com_hash_bcrypt(sessionmaker_teste, db, monkeypatch, capsys):
    _senhas(monkeypatch, SENHA, SENHA)
    assert criar_admin.main(["--usuario", "CECP0002"]) == 0
    a = db.execute(select(Administrador)).scalar_one()
    assert a.usuario == "cecp0002" and a.senha_hash.startswith("$2b$") and SENHA not in a.senha_hash
    assert SENHA not in capsys.readouterr().out


def test_senhas_diferentes_nao_criam(sessionmaker_teste, db, monkeypatch):
    _senhas(monkeypatch, SENHA, "outra-senha-123")
    with pytest.raises(SystemExit):
        criar_admin.main(["--usuario", "CECP0002"])
    assert db.execute(select(Administrador)).first() is None


def test_senha_fraca_nao_cria(sessionmaker_teste, db, monkeypatch):
    _senhas(monkeypatch, "curta", "curta")
    assert criar_admin.main(["--usuario", "CECP0002"]) == 1
    assert db.execute(select(Administrador)).first() is None


def test_usuario_duplicado_exige_flag(sessionmaker_teste, admin, monkeypatch):
    assert criar_admin.main(["--usuario", "cecp0001"]) == 1


def test_redefinir_troca_senha_e_encerra_sessoes(sessionmaker_teste, db, admin, monkeypatch):
    services.iniciar_sessao(db, admin)
    antigo = admin.senha_hash
    _senhas(monkeypatch, "nova-senha-forte-9", "nova-senha-forte-9")
    assert criar_admin.main(["--usuario", "CECP0001", "--redefinir-senha"]) == 0
    db.expire_all()
    assert db.get(Administrador, admin.id).senha_hash != antigo
    assert all(t.revogado_em for t in db.execute(select(RefreshToken)).scalars())


def test_redefinir_usuario_inexistente(sessionmaker_teste, monkeypatch):
    assert criar_admin.main(["--usuario", "ninguem", "--redefinir-senha"]) == 1
