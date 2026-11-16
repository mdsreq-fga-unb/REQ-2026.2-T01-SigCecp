"""Regras de negócio da autenticação do administrador"""

import logging
import unicodedata
import uuid
from dataclasses import dataclass
from datetime import datetime, timedelta

from sqlalchemy import delete, select, update
from sqlalchemy.orm import Session

from backend.auth import security
from backend.auth import settings as cfg
from backend.auth.models import Administrador, RefreshToken
from backend.auth.tempo import agora, como_utc

logger = logging.getLogger("sigcecp.auth")

USUARIO_MAX = 50


class CredenciaisInvalidas(Exception):
    """Falha de login que não revela se o usuário
    existe, se a senha estava errada ou se a conta está bloqueada."""


class RefreshInvalido(Exception):
    def __init__(self, motivo: str, limpar_cookies: bool = True):
        super().__init__(motivo)
        self.motivo = motivo
        self.limpar_cookies = limpar_cookies


@dataclass(frozen=True)
class SessaoEmitida:
    familia: str
    access_token: str
    access_max_age: int   # em segundos
    refresh_token: str
    refresh_max_age: int  # em segundos


def normalizar_usuario(usuario: str) -> str:
    return unicodedata.normalize("NFKC", usuario).strip().casefold()


def autenticar(db: Session, usuario: str, senha: str) -> Administrador:
    momento = agora()
    nome = normalizar_usuario(usuario)

    admin = None
    if nome and len(nome) <= USUARIO_MAX:
        admin = db.execute(
            select(Administrador).where(Administrador.usuario == nome)
        ).scalar_one_or_none()

    if admin is None:
        security.gastar_tempo_de_verificacao()
        raise CredenciaisInvalidas()

    bloqueado_ate = como_utc(admin.bloqueado_ate)
    if bloqueado_ate is not None and bloqueado_ate > momento:
        security.gastar_tempo_de_verificacao()
        logger.warning("Login recusado: conta bloqueada (admin_id=%s)", admin.id)
        raise CredenciaisInvalidas()

    if not security.verificar_senha(senha, admin.senha_hash):
        _registrar_falha(db, admin, momento)
        raise CredenciaisInvalidas()

    if not admin.ativo:
        raise CredenciaisInvalidas()

    admin.tentativas_falhas = 0
    admin.bloqueado_ate = None
    admin.ultimo_login_em = momento
    if security.hash_precisa_atualizar(admin.senha_hash):
        admin.senha_hash = security.gerar_hash(senha)
    db.commit()
    return admin


def _registrar_falha(db: Session, admin: Administrador, momento: datetime) -> None:
    s = cfg.settings
    db.execute(
        update(Administrador)
        .where(Administrador.id == admin.id)
        .values(tentativas_falhas=Administrador.tentativas_falhas + 1)
    )
    db.flush()
    db.refresh(admin)
    logger.warning("Falha de login (admin_id=%s, tentativas=%s)", admin.id, admin.tentativas_falhas)
    if admin.tentativas_falhas >= s.login_max_tentativas:
        admin.bloqueado_ate = momento + s.login_bloqueio
        admin.tentativas_falhas = 0
        logger.warning("Conta bloqueada por %s (admin_id=%s)", s.login_bloqueio, admin.id)
    db.commit()

def iniciar_sessao(db: Session, admin: Administrador) -> SessaoEmitida:
    momento = agora()
    db.execute(delete(RefreshToken).where(RefreshToken.expira_em < momento - timedelta(days=1)))
    sessao = _emitir(db, admin, uuid.uuid4().hex, momento, momento)
    db.commit()
    return sessao


def _emitir(
    db: Session, admin: Administrador, familia: str, sessao_iniciada_em: datetime, momento: datetime,
) -> SessaoEmitida:
    s = cfg.settings
    refresh = security.novo_refresh_token()
    expira = min(momento + s.refresh_ttl, sessao_iniciada_em + s.sessao_max)
    db.add(RefreshToken(
        administrador_id=admin.id,
        familia=familia,
        token_hash=security.hash_token(refresh),
        criado_em=momento,
        expira_em=expira,
        sessao_iniciada_em=sessao_iniciada_em,
    ))
    access, _ = security.criar_access_token(admin.id, familia)
    return SessaoEmitida(
        familia=familia,
        access_token=access,
        access_max_age=int(s.access_ttl.total_seconds()),
        refresh_token=refresh,
        refresh_max_age=max(int((expira - momento).total_seconds()), 0),
    )


def validar_sessao(db: Session, admin_id: int, sid: str) -> Administrador | None:
    admin = db.get(Administrador, admin_id)
    if admin is None or not admin.ativo:
        return None
    vigente = db.execute(
        select(RefreshToken.id).where(
            RefreshToken.familia == sid,
            RefreshToken.administrador_id == admin_id,
            RefreshToken.usado_em.is_(None),
            RefreshToken.revogado_em.is_(None),
            RefreshToken.expira_em > agora(),
        ).limit(1)
    ).first()
    return admin if vigente else None


def renovar_sessao(db: Session, refresh_token: str) -> SessaoEmitida:
    s = cfg.settings
    momento = agora()

    registro = db.execute(
        select(RefreshToken).where(RefreshToken.token_hash == security.hash_token(refresh_token))
    ).scalar_one_or_none()

    if registro is None:
        raise RefreshInvalido("token desconhecido")
    if registro.revogado_em is not None:
        raise RefreshInvalido("token revogado")

    if registro.usado_em is not None:
        if momento - como_utc(registro.usado_em) <= s.refresh_reuse_grace:
            raise RefreshInvalido("requisição paralela", limpar_cookies=False)
        _revogar_familia(db, registro.familia, momento)
        db.commit()
        logger.warning(
            "Reuso de refresh token: família %s revogada (admin_id=%s)",
            registro.familia, registro.administrador_id,
        )
        raise RefreshInvalido("reuso detectado")

    if como_utc(registro.expira_em) <= momento:
        raise RefreshInvalido("token expirado")

    admin = db.get(Administrador, registro.administrador_id)
    if admin is None or not admin.ativo:
        _revogar_familia(db, registro.familia, momento)
        db.commit()
        raise RefreshInvalido("administrador inativo")

    consumido = db.execute(
        update(RefreshToken)
        .where(
            RefreshToken.id == registro.id,
            RefreshToken.usado_em.is_(None),
            RefreshToken.revogado_em.is_(None),
        )
        .values(usado_em=momento)
    )
    if consumido.rowcount != 1:
        db.rollback()
        raise RefreshInvalido("requisição paralela", limpar_cookies=False)

    sessao = _emitir(db, admin, registro.familia, como_utc(registro.sessao_iniciada_em), momento)
    db.commit()
    return sessao


def familia_do_refresh(db: Session, refresh_token: str) -> str | None:
    return db.execute(
        select(RefreshToken.familia).where(RefreshToken.token_hash == security.hash_token(refresh_token))
    ).scalar_one_or_none()


def encerrar_sessao(db: Session, familia: str) -> None:
    _revogar_familia(db, familia, agora())
    db.commit()


def _revogar_familia(db: Session, familia: str, momento: datetime) -> None:
    db.execute(
        update(RefreshToken)
        .where(RefreshToken.familia == familia, RefreshToken.revogado_em.is_(None))
        .values(revogado_em=momento)
    )


def criar_administrador(db: Session, usuario: str, senha: str) -> Administrador:
    nome = normalizar_usuario(usuario)
    if not (3 <= len(nome) <= USUARIO_MAX):
        raise ValueError(f"O usuário deve ter entre 3 e {USUARIO_MAX} caracteres.")
    admin = Administrador(usuario=nome, senha_hash=security.hash_senha(senha), ativo=True)
    db.add(admin)
    db.commit()
    return admin


def redefinir_senha(db: Session, admin: Administrador, nova_senha: str) -> None:
    admin.senha_hash = security.hash_senha(nova_senha)
    admin.tentativas_falhas = 0
    admin.bloqueado_ate = None
    db.execute(
        update(RefreshToken)
        .where(RefreshToken.administrador_id == admin.id, RefreshToken.revogado_em.is_(None))
        .values(revogado_em=agora())
    )
    db.commit()
