from datetime import timedelta

import pytest
from fastapi.routing import APIRoute
from sqlalchemy import select

from backend.auth import services
from backend.auth import settings as cfg
from backend.auth.dependencies import exigir_admin
from backend.auth.models import Administrador, RefreshToken
from backend.auth.tempo import agora, como_utc
from backend.main import app
from conftest import (
    SENHA,
    USUARIO,
    access_com_expiracao,
    cookies_set,
    logar,
    token_csrf,
    trocar_cookie,
    valor_cookie,
)

pytestmark = pytest.mark.auth_real

ACCESS, REFRESH = "sigcecp_access", "sigcecp_refresh"
HTML = {"accept": "text/html"}


def test_todas_as_rotas_administrativas_exigem_admin():
    desprotegidas = []
    for r in app.routes:
        if (
            isinstance(r, APIRoute)
            and r.path.startswith("/coordenacao")
            and not r.path.startswith("/coordenacao/auth")
            and not any(d.call is exigir_admin for d in r.dependant.dependencies)
        ):
            desprotegidas.append(r.path)
    assert desprotegidas == []


@pytest.mark.parametrize("caminho", ["/", "/eventos"])
def test_rotas_publicas_nao_exigem_login(client, caminho):
    assert client.get(caminho).status_code == 200


def test_rotas_publicas_nao_recebem_cabecalhos_do_painel(client):
    r = client.get("/")
    assert "no-store" not in r.headers.get("cache-control", "")
    assert "x-frame-options" not in r.headers


@pytest.mark.parametrize(("metodo", "caminho"), [
    ("get", "/coordenacao/conteudo"), ("get", "/coordenacao/eventos"),
    ("get", "/coordenacao/eventos/novo"), ("post", "/coordenacao/conteudo/novo"),
    ("post", "/coordenacao/eventos/1/remover"),
])
def test_admin_sem_login_retorna_401(client, metodo, caminho):
    r = getattr(client, metodo)(caminho)
    assert r.status_code == 401
    assert r.json() == {"detail": "Autenticação necessária."}


def test_navegador_sem_login_ve_pagina_de_acesso_restrito(client):
    r = client.get("/coordenacao/conteudo", headers=HTML)
    assert r.status_code == 401
    assert "Acesso restrito" in r.text and "/coordenacao/auth/login" in r.text


def test_cabecalhos_de_protecao_na_area_admin(client):
    r = client.get("/coordenacao/conteudo")
    assert r.headers["cache-control"] == "no-store"
    assert r.headers["x-frame-options"] == "DENY"


# ---------- login ----------
def test_pagina_de_login_e_publica(client):
    r = client.get("/coordenacao/auth/login")
    assert r.status_code == 200 and 'name="senha"' in r.text


def test_login_ok_define_cookies_seguros(client, admin):
    r = logar(client)
    assert r.status_code == 303 and r.headers["location"] == "/coordenacao"
    c = cookies_set(r)
    for nome in (ACCESS, REFRESH):
        bruto = c[nome]
        assert "HttpOnly" in bruto
        assert "SameSite=strict" in bruto
        assert "Path=/coordenacao" in bruto
    assert "Max-Age=900" in c[ACCESS]
    assert "Max-Age=604800" in c[REFRESH]
    assert "Secure" not in c[ACCESS]


def test_cookies_ganham_secure_em_producao(client, admin, monkeypatch):
    from dataclasses import replace
    monkeypatch.setattr(cfg, "settings", replace(cfg.settings, cookie_secure=True))
    c = cookies_set(logar(client))
    assert "Secure" in c[ACCESS] and "Secure" in c[REFRESH]


def test_login_aceita_usuario_sem_diferenciar_caixa_e_espacos(client, admin):
    assert logar(client, usuario="  cecp0001 ").status_code == 303


def test_login_falho_nao_revela_o_motivo_nem_define_cookies(client, admin):
    erradas = [
        logar(client, senha="errada-errada-1"),
        logar(client, usuario="naoexiste"),
    ]
    assert all(r.status_code == 401 for r in erradas)
    assert erradas[0].text.count("Usuário ou senha inválidos") == 1
    corpos = {r.text.replace("naoexiste", "").replace(USUARIO, "") for r in erradas}
    assert len(corpos) == 1
    assert not any(cookies_set(r) for r in erradas)


def test_login_nao_ecoa_a_senha_e_escapa_o_usuario(client, admin):
    r = logar(client, usuario='"><script>alert(1)</script>', senha="segredo-segredo-1")
    assert "segredo-segredo-1" not in r.text
    assert "<script>alert(1)</script>" not in r.text


def test_bloqueio_apos_tentativas_e_liberacao_por_tempo(client, admin, db):
    for _ in range(3):
        assert logar(client, senha="errada-errada-1").status_code == 401
    assert logar(client).status_code == 401
    db.expire_all()
    a = db.get(Administrador, admin.id)
    a.bloqueado_ate = agora() - timedelta(seconds=1)
    db.commit()
    assert logar(client).status_code == 303


def test_login_origem_externa_e_recusado(client, admin):
    r = client.post(
        "/coordenacao/auth/login",
        data={"usuario": USUARIO, "senha": SENHA},
        headers={"origin": "https://evil.example"},
    )
    assert r.status_code == 403 and not cookies_set(r)


def test_login_origem_propria_e_aceita(client, admin):
    r = client.post(
        "/coordenacao/auth/login",
        data={"usuario": USUARIO, "senha": SENHA},
        headers={"origin": "http://testserver"},
    )
    assert r.status_code == 303


def test_senha_nunca_e_gravada_em_texto_puro(client, admin, db):
    a = db.get(Administrador, admin.id)
    assert a.senha_hash.startswith("$2b$") and SENHA not in a.senha_hash


# ---------- acesso autenticado ----------
def test_admin_autenticado_acessa_e_formularios_trazem_csrf(client, admin):
    logar(client)
    assert client.get("/coordenacao/conteudo").status_code == 200
    assert token_csrf(client)
    assert '/coordenacao/auth/logout"' in client.get("/coordenacao/eventos").text


def test_access_adulterado_nao_autoriza_por_si_so(client, admin):
    logar(client)
    client.cookies.delete(REFRESH, path="/coordenacao")
    trocar_cookie(client, ACCESS, valor_cookie(client, ACCESS)[:-3] + "AAA")
    assert client.get("/coordenacao/conteudo").status_code == 401


def test_access_adulterado_com_refresh_valido_e_descartado_e_renovado(client, admin):
    logar(client)
    adulterado = valor_cookie(client, ACCESS)[:-3] + "AAA"
    trocar_cookie(client, ACCESS, adulterado)
    r = client.get("/coordenacao/conteudo")
    assert r.status_code == 200 and valor_cookie(client, ACCESS) != adulterado


def test_access_forjado_sem_sessao_no_banco_e_recusado(client, admin):
    forjado = access_com_expiracao(admin.id, "sidfalso", 600)
    client.cookies.set(ACCESS, forjado, path="/coordenacao")
    assert client.get("/coordenacao/conteudo").status_code == 401


# ---------- CSRF ----------
def _novo(client, **extra):
    return client.post("/coordenacao/conteudo/novo", data={"titulo": "Teste", **extra})


def test_post_sem_csrf_e_recusado(client, admin):
    logar(client)
    assert _novo(client).status_code == 403


def test_post_com_csrf_invalido_e_recusado(client, admin):
    logar(client)
    assert _novo(client, csrf_token="x.y").status_code == 403


def test_post_com_csrf_de_outra_sessao_e_recusado(client, admin):
    from backend.auth import csrf
    logar(client)
    assert _novo(client, csrf_token=csrf.gerar_token("outra-sessao")).status_code == 403


def test_post_com_csrf_valido_funciona(client, admin):
    logar(client)
    r = _novo(client, csrf_token=token_csrf(client))
    assert r.status_code == 303
    assert r.headers["location"].endswith("/coordenacao/conteudo")


def test_csrf_aceito_no_cabecalho(client, admin):
    logar(client)
    r = client.post("/coordenacao/conteudo/novo", data={"titulo": "T"},
                    headers={"x-csrf-token": token_csrf(client)})
    assert r.status_code == 303


def test_csrf_valido_mas_origem_externa_e_recusado(client, admin):
    logar(client)
    r = _novo(client, csrf_token=token_csrf(client))
    assert r.status_code == 303
    r = client.post(
        "/coordenacao/conteudo/novo",
        data={"titulo": "T", "csrf_token": token_csrf(client)},
        headers={"origin": "https://evil.example"},
    )
    assert r.status_code == 403


def test_csrf_em_upload_multipart(client, admin):
    logar(client)
    token = token_csrf(client)
    sem = client.post("/coordenacao/conteudo/novo", data={"titulo": "T"},
                      files={"imagem": ("a.png", b"x", "image/png")})
    com = client.post(
        "/coordenacao/conteudo/novo",
        data={"titulo": "T", "csrf_token": token},
        files={"video": ("", b"", "application/octet-stream")},
    )
    assert sem.status_code == 403 and com.status_code == 303


def test_get_nao_exige_csrf(client, admin):
    logar(client)
    assert client.get("/coordenacao/conteudo").status_code == 200


# ---------- renovação transparente ----------
def _familia(db):
    db.expire_all()
    return db.execute(select(RefreshToken).order_by(RefreshToken.id)).scalars().all()


def test_access_expirado_e_renovado_com_rotacao_do_refresh(client, admin, db):
    logar(client)
    antigo_refresh = valor_cookie(client, REFRESH)
    csrf_antes = token_csrf(client)
    sid = _familia(db)[0].familia
    trocar_cookie(client, ACCESS, access_com_expiracao(admin.id, sid, -60))

    r = client.get("/coordenacao/conteudo")
    assert r.status_code == 200
    novos = cookies_set(r)
    assert ACCESS in novos and REFRESH in novos
    assert valor_cookie(client, REFRESH) != antigo_refresh
    linhas = _familia(db)
    assert len(linhas) == 2
    assert linhas[0].usado_em is not None
    assert linhas[1].usado_em is None
    assert _novo(client, csrf_token=csrf_antes).status_code == 303


def test_post_apos_expirar_o_access_nao_perde_o_formulario(client, admin, db):
    logar(client)
    token = token_csrf(client)
    sid = _familia(db)[0].familia
    trocar_cookie(client, ACCESS, access_com_expiracao(admin.id, sid, -1))
    r = _novo(client, csrf_token=token)
    assert r.status_code == 303 and ACCESS in cookies_set(r)


def test_cookie_de_access_ausente_tambem_renova(client, admin):
    logar(client)
    client.cookies.delete(ACCESS, path="/coordenacao")
    assert client.get("/coordenacao/conteudo").status_code == 200


def test_refresh_expirado_exige_novo_login_e_limpa_cookies(client, admin, db):
    logar(client)
    sid = _familia(db)[0].familia
    linha = _familia(db)[0]
    linha.expira_em = agora() - timedelta(seconds=1)
    db.commit()
    trocar_cookie(client, ACCESS, access_com_expiracao(admin.id, sid, -60))
    r = client.get("/coordenacao/conteudo")
    assert r.status_code == 401
    assert "Max-Age=0" in cookies_set(r)[REFRESH]


def test_teto_absoluto_da_sessao_limita_a_rotacao(db, admin, monkeypatch):
    from dataclasses import replace
    monkeypatch.setattr(
        cfg, "settings", replace(cfg.settings, sessao_max=timedelta(days=1))
    )
    s1 = services.iniciar_sessao(db, admin)
    s2 = services.renovar_sessao(db, s1.refresh_token)
    ultima = _familia(db)[-1]
    limite = como_utc(ultima.sessao_iniciada_em) + timedelta(days=1)
    assert como_utc(ultima.expira_em) <= limite
    assert s2.refresh_max_age <= 86400


# ---------- /refresh explícito ----------
def test_refresh_explicito_rotaciona_e_exige_csrf(client, admin, db):
    logar(client)
    token = token_csrf(client)
    antigo = valor_cookie(client, REFRESH)

    assert client.post("/coordenacao/auth/refresh").status_code == 403
    r = client.post("/coordenacao/auth/refresh", headers={"x-csrf-token": token})
    assert r.status_code == 204
    assert cookies_set(r).keys() >= {ACCESS, REFRESH}
    assert valor_cookie(client, REFRESH) != antigo


def test_refresh_sem_cookie_retorna_401(client, admin):
    assert client.post("/coordenacao/auth/refresh").status_code == 401


def test_refresh_com_origem_externa_e_recusado(client, admin):
    logar(client)
    r = client.post(
        "/coordenacao/auth/refresh",
        headers={"origin": "https://evil.example"},
    )
    assert r.status_code == 403


def test_reaproveitar_refresh_dentro_da_tolerancia_nao_derruba_a_sessao(db, admin):
    s1 = services.iniciar_sessao(db, admin)
    services.renovar_sessao(db, s1.refresh_token)
    with pytest.raises(services.RefreshInvalido) as e:
        services.renovar_sessao(db, s1.refresh_token)
    assert e.value.limpar_cookies is False
    assert _familia(db)[-1].revogado_em is None


def test_reuso_de_refresh_revoga_a_familia_inteira(db, admin, monkeypatch):
    from dataclasses import replace
    monkeypatch.setattr(
        cfg, "settings", replace(cfg.settings, refresh_reuse_grace=timedelta(0))
    )
    s1 = services.iniciar_sessao(db, admin)
    s2 = services.renovar_sessao(db, s1.refresh_token)
    with pytest.raises(services.RefreshInvalido, match="reuso"):
        services.renovar_sessao(db, s1.refresh_token)
    assert all(linha.revogado_em is not None for linha in _familia(db))
    with pytest.raises(services.RefreshInvalido):
        services.renovar_sessao(db, s2.refresh_token)
    assert services.validar_sessao(db, admin.id, s1.familia) is None


# ---------- logout ----------
def test_logout_revoga_no_servidor_e_limpa_cookies(client, admin):
    logar(client)
    token = token_csrf(client)
    access_antigo = valor_cookie(client, ACCESS)

    r = client.post("/coordenacao/auth/logout", data={"csrf_token": token})
    assert r.status_code == 303 and r.headers["location"] == "/coordenacao/auth/login"
    c = cookies_set(r)
    assert "Max-Age=0" in c[ACCESS] and "Max-Age=0" in c[REFRESH]

    client.cookies.set(ACCESS, access_antigo, path="/coordenacao")
    assert client.get("/coordenacao/conteudo").status_code == 401


def test_logout_sem_csrf_e_recusado_e_sessao_continua(client, admin):
    logar(client)
    assert client.post("/coordenacao/auth/logout").status_code == 403
    assert client.get("/coordenacao/conteudo").status_code == 200


def test_logout_sem_sessao_e_idempotente(client, admin):
    r = client.post("/coordenacao/auth/logout")
    assert r.status_code == 303


def test_admin_desativado_perde_acesso_imediatamente(client, admin, db):
    logar(client)
    db.get(Administrador, admin.id).ativo = False
    db.commit()
    assert client.get("/coordenacao/conteudo").status_code == 401


def test_trocar_a_senha_encerra_as_sessoes(client, admin, db):
    logar(client)
    services.redefinir_senha(db, db.get(Administrador, admin.id), "nova-senha-forte-9")
    assert client.get("/coordenacao/conteudo").status_code == 401
    assert logar(client).status_code == 401
    assert logar(client, senha="nova-senha-forte-9").status_code == 303


def test_novo_login_encerra_a_sessao_anterior_do_navegador(client, admin, db):
    logar(client)
    primeira = _familia(db)[0].familia
    logar(client)
    db.expire_all()
    assert services.validar_sessao(db, admin.id, primeira) is None
