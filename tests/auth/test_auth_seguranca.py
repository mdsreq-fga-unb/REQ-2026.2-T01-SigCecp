from dataclasses import replace
from datetime import timedelta

import pytest
from jose import jwt

from backend.auth import csrf, security
from backend.auth import settings as cfg

pytestmark = pytest.mark.auth_real


# ---------- senha ----------
def test_hash_e_bcrypt_com_salt_e_nunca_texto_puro():
    h1, h2 = security.hash_senha("uma-senha-bem-longa"), security.hash_senha("uma-senha-bem-longa")
    assert h1.startswith("$2b$") and len(h1) == 60
    assert "uma-senha-bem-longa" not in h1
    assert h1 != h2


def test_verificar_senha():
    h = security.hash_senha("uma-senha-bem-longa")
    assert security.verificar_senha("uma-senha-bem-longa", h)
    assert not security.verificar_senha("outra-senha-longa", h)
    assert not security.verificar_senha("x", "isso-nao-e-um-hash")


def test_senha_acima_de_72_bytes_e_tratada_sem_excecao():
    longa = "a" * 100
    with pytest.raises(security.SenhaInvalida):
        security.hash_senha(longa)
    h = security.hash_senha("uma-senha-bem-longa")
    assert security.verificar_senha(longa, h) is False


@pytest.mark.parametrize("senha", ["curta", "a\x00" + "b" * 20])
def test_politica_recusa_senha_fraca(senha):
    with pytest.raises(security.SenhaInvalida):
        security.validar_politica_senha(senha)


def test_politica_recusa_senha_igual_ao_usuario():
    with pytest.raises(security.SenhaInvalida):
        security.validar_politica_senha("cecp0001cecp", "CECP0001CECP")


def test_hash_com_custo_antigo_pede_atualizacao(monkeypatch):
    h = security.hash_senha("uma-senha-bem-longa")
    assert not security.hash_precisa_atualizar(h)
    monkeypatch.setattr(cfg, "settings", replace(cfg.settings, bcrypt_rounds=6))
    assert security.hash_precisa_atualizar(h)


# ---------- JWT ----------
def test_access_token_ida_e_volta():
    token, _ = security.criar_access_token(7, "abc")
    claims = security.decodificar_access_token(token)
    assert claims["sub"] == "7" and claims["sid"] == "abc"


def _assinar(claims_extra=None, chave=None, alg="HS256", remover=()):
    s = cfg.settings
    claims = {"sub": "1", "sid": "x", "typ": "access", "iss": s.jwt_emissor, "aud": s.jwt_audiencia,
              "iat": 1, "exp": 4102444800}
    claims.update(claims_extra or {})
    for k in remover:
        claims.pop(k)
    return jwt.encode(claims, chave or s.jwt_key, algorithm=alg)


def test_jwt_valido_de_referencia():
    assert security.decodificar_access_token(_assinar()) is not None


@pytest.mark.parametrize("token", [
    "",
    "lixo",
    "a.b.c",
])
def test_jwt_malformado(token):
    assert security.decodificar_access_token(token) is None


def test_jwt_expirado():
    assert security.decodificar_access_token(_assinar({"exp": 1})) is None


def test_jwt_assinado_com_outra_chave():
    assert security.decodificar_access_token(_assinar(chave=b"outra-chave" * 4)) is None


def test_jwt_adulterado_no_payload():
    cabecalho, payload, assinatura = _assinar().split(".")
    outro = _assinar({"sub": "999"}).split(".")[1]
    assert security.decodificar_access_token(f"{cabecalho}.{outro}.{assinatura}") is None


def test_jwt_alg_none_e_rejeitado():
    import base64, json
    b64 = lambda d: base64.urlsafe_b64encode(json.dumps(d).encode()).rstrip(b"=").decode()
    s = cfg.settings
    token = f"{b64({'alg': 'none', 'typ': 'JWT'})}.{b64({'sub': '1', 'sid': 'x', 'typ': 'access', 'iss': s.jwt_emissor, 'aud': s.jwt_audiencia, 'iat': 1, 'exp': 4102444800})}."
    assert security.decodificar_access_token(token) is None


@pytest.mark.parametrize("extra", [{"aud": "outro"}, {"iss": "outro"}, {"typ": "refresh"}, {"sub": "abc"}, {"sid": 5}])
def test_jwt_claims_incorretas(extra):
    assert security.decodificar_access_token(_assinar(extra)) is None


@pytest.mark.parametrize("faltando", ["exp", "iat", "sub", "iss", "aud"])
def test_jwt_sem_claim_obrigatoria(faltando):
    assert security.decodificar_access_token(_assinar(remover=(faltando,))) is None


# ---------- CSRF ----------
def test_csrf_valido_apenas_para_a_propria_sessao():
    t = csrf.gerar_token("sessao-A")
    assert csrf.validar_token(t, "sessao-A")
    assert not csrf.validar_token(t, "sessao-B")


def test_csrf_muda_a_cada_geracao_mas_ambos_validam():
    a, b = csrf.gerar_token("s"), csrf.gerar_token("s")
    assert a != b and csrf.validar_token(a, "s") and csrf.validar_token(b, "s")


@pytest.mark.parametrize("token", ["", ".", "abc", "abc.def", "." + "a" * 64, "a" * 500])
def test_csrf_invalido(token):
    assert not csrf.validar_token(token, "s")


def test_csrf_adulterado():
    nonce, mac = csrf.gerar_token("s").split(".")
    trocado = ("0" if mac[0] != "0" else "1") + mac[1:]
    assert not csrf.validar_token(f"{nonce}.{trocado}", "s")
    assert not csrf.validar_token(f"{'0' * 32}.{mac}", "s")


def test_chaves_de_jwt_e_csrf_sao_distintas():
    assert cfg.settings.jwt_key != cfg.settings.csrf_key


# ---------- settings ----------
def _env(monkeypatch, **valores):
    for k in ("APP_ENV", "AUTH_SECRET_KEY", "COOKIE_SECURE", "COOKIE_SAMESITE"):
        monkeypatch.delenv(k, raising=False)
    for k, v in valores.items():
        monkeypatch.setenv(k, v)


def test_producao_exige_segredo(monkeypatch):
    _env(monkeypatch, APP_ENV="production")
    with pytest.raises(RuntimeError, match="AUTH_SECRET_KEY"):
        cfg.Settings.from_env()


def test_segredo_curto_e_recusado(monkeypatch):
    _env(monkeypatch, AUTH_SECRET_KEY="curta")
    with pytest.raises(RuntimeError, match="curta"):
        cfg.Settings.from_env()


def test_producao_nao_aceita_cookie_sem_secure(monkeypatch):
    _env(monkeypatch, APP_ENV="production", AUTH_SECRET_KEY="s" * 40, COOKIE_SECURE="false")
    with pytest.raises(RuntimeError, match="COOKIE_SECURE"):
        cfg.Settings.from_env()


def test_samesite_none_exige_secure(monkeypatch):
    _env(monkeypatch, AUTH_SECRET_KEY="s" * 40, COOKIE_SAMESITE="none")
    with pytest.raises(RuntimeError, match="none"):
        cfg.Settings.from_env()


def test_padroes_por_ambiente(monkeypatch):
    _env(monkeypatch, APP_ENV="production", AUTH_SECRET_KEY="s" * 40)
    prod = cfg.Settings.from_env()
    assert prod.cookie_secure and prod.cookie_samesite == "strict"
    assert prod.access_ttl == timedelta(minutes=15)
    _env(monkeypatch)
    dev = cfg.Settings.from_env()
    assert not dev.cookie_secure
