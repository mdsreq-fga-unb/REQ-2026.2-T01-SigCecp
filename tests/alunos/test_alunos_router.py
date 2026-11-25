"""Ficha do aluno (RF21 a RF24) e associação à turma (RF06), pelos critérios de aceitação das fichas."""
import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

import backend.auth.models  # noqa: F401  (registra as tabelas de autenticação)
from backend.alunos import arquivos
from backend.alunos.models import Aluno
from backend.alunos.schemas import QUESTOES
from backend.auth.csrf import verificar_csrf
from backend.auth.dependencies import exigir_admin
from backend.database import Base, get_db
from backend.main import app
from backend.turmas.models import Turma

BASE = "/coordenacao/alunos"
PNG = b"\x89PNG\r\n\x1a\n" + b"0" * 64
PDF = b"%PDF-1.4 laudo de exemplo"


@pytest.fixture
def ambiente(tmp_path, monkeypatch):
    monkeypatch.setattr(arquivos, "DIRETORIO_ARQUIVOS", tmp_path / "arquivos")
    engine = create_engine(
        f"sqlite:///{(tmp_path / 'alunos.db').as_posix()}",
        connect_args={"check_same_thread": False},
    )
    Base.metadata.create_all(engine)
    sessoes = sessionmaker(bind=engine, autoflush=False)

    def sessao_temporaria():
        with sessoes() as db:
            yield db

    app.dependency_overrides[get_db] = sessao_temporaria
    app.dependency_overrides[exigir_admin] = lambda: object()
    app.dependency_overrides[verificar_csrf] = lambda: None
    try:
        with TestClient(app, follow_redirects=False) as cliente:
            yield cliente, sessoes, engine
    finally:
        app.dependency_overrides.clear()
        engine.dispose()


def nova_turma(cliente, modalidade="Judô", dias=("segunda", "quarta")):
    cliente.post("/coordenacao/turmas/novo", data={
        "modalidade": modalidade, "dias": list(dias), "inicio": "14:00", "termino": "15:00",
    })


def ids_das_turmas(sessoes):
    with sessoes() as db:
        return [t.id for t in db.query(Turma).order_by(Turma.id)]


def ficha(turma, **alteracoes):
    dados = {
        "nome": "Ana Clara de Oliveira Santos",
        "data_inicio": "2026-02-02",
        "documento_identificacao": "RG 4.567.890 SSP/DF",
        "nome_mae": "Maria de Oliveira Santos",
        "telefone_mae": "(61) 99999-0102",
        "celular": "(61) 99999-0101",
        "tipo_escola": "publica",
        "graduacao": "Amarela",
        "problema_saude": "nao",
        "turma_id": str(turma),
        "responsavel_nome": "Maria de Oliveira Santos",
        "termo_aceito": "sim",
    }
    dados |= {codigo: "nao" for codigo, _, _ in QUESTOES}
    dados.update(alteracoes)
    return {chave: valor for chave, valor in dados.items() if valor is not None}


def cadastrar(cliente, sessoes, arquivos_enviados=None, **alteracoes):
    nova_turma(cliente)
    turma_id = ids_das_turmas(sessoes)[0]
    resposta = cliente.post(f"{BASE}/novo", data=ficha(turma_id, **alteracoes), files=arquivos_enviados)
    assert resposta.status_code == 303, resposta.text
    return int(resposta.headers["location"].split("/")[-1].split("?")[0])


def aluno_no_banco(sessoes, aluno_id):
    with sessoes() as db:
        aluno = db.get(Aluno, aluno_id)
        _ = aluno.associacoes, aluno.documentos
        for a in aluno.associacoes:
            _ = a.turma
        return aluno


# ---------- RF21: cadastrar aluno ----------

def test_formulario_de_cadastro(ambiente):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    resposta = cliente.get(f"{BASE}/novo")

    assert resposta.status_code == 200
    assert 'enctype="multipart/form-data"' in resposta.text
    assert "Judô • Segunda e quarta-feira • 14h às 15h" in resposta.text
    assert "Uso de imagem" in resposta.text
    assert "centroesportivocecp@gmail.com" in resposta.text


def test_cadastro_sem_turma_cadastrada_avisa(ambiente):
    cliente, _, _ = ambiente

    resposta = cliente.get(f"{BASE}/novo")

    assert "Cadastre uma turma antes" in resposta.text


def test_criterio_1_cadastra_com_todos_os_obrigatorios(ambiente):
    cliente, sessoes, _ = ambiente

    aluno_id = cadastrar(cliente, sessoes)

    aluno = aluno_no_banco(sessoes, aluno_id)
    assert aluno.nome == "Ana Clara de Oliveira Santos"
    assert aluno.ativo
    assert aluno.termo_aceito_em is not None
    assert aluno.vinculo_atual.turma.modalidade == "Judô"


@pytest.mark.parametrize("campo", ["nome", "data_inicio", "documento_identificacao", "nome_mae", "telefone_mae", "celular", "graduacao", "responsavel_nome"])
def test_criterio_2_campo_obrigatorio_vazio_bloqueia_e_indica(ambiente, campo):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    resposta = cliente.post(f"{BASE}/novo", data=ficha(ids_das_turmas(sessoes)[0], **{campo: ""}))

    assert resposta.status_code == 422
    assert "Cadastro não realizado" in resposta.text
    assert f'id="erro-{campo}"' in resposta.text
    with sessoes() as db:
        assert db.query(Aluno).count() == 0


def test_criterio_2_sem_turma_bloqueia(ambiente):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    resposta = cliente.post(f"{BASE}/novo", data=ficha(ids_das_turmas(sessoes)[0], turma_id=""))

    assert resposta.status_code == 422
    assert "Escolha a turma" in resposta.text


def test_criterio_3_questionario_incompleto_nao_libera(ambiente):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    resposta = cliente.post(f"{BASE}/novo", data=ficha(ids_das_turmas(sessoes)[0], q4=None, q9=None))

    assert resposta.status_code == 422
    assert "Faltam: 4, 9." in resposta.text
    with sessoes() as db:
        assert db.query(Aluno).count() == 0


def test_sem_aceite_do_termo_nao_cadastra(ambiente):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    resposta = cliente.post(f"{BASE}/novo", data=ficha(ids_das_turmas(sessoes)[0], termo_aceito=None))

    assert resposta.status_code == 422
    assert "aceite do termo" in resposta.text
    with sessoes() as db:
        assert db.query(Aluno).count() == 0


def test_termo_inclui_o_uso_de_imagem_como_condicao(ambiente):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    html = cliente.get(f"{BASE}/novo").text

    assert "Esta autorização é condição para o cadastro" in html
    assert 'name="uso_imagem"' not in html


def test_cadastro_grava_a_versao_do_termo(ambiente):
    cliente, sessoes, _ = ambiente

    aluno = aluno_no_banco(sessoes, cadastrar(cliente, sessoes))

    assert aluno.termo_versao == "1.0-provisoria"


def test_ficha_mostra_o_registro_dos_consentimentos(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes, responsavel_cpf="123.456.789-00")

    html = cliente.get(f"{BASE}/{aluno_id}").text

    assert "Aceite dado por" in html
    assert "Maria de Oliveira Santos (CPF 123.456.789-00)" in html
    assert "Versão do termo" in html
    assert "Termo (responsabilidade, dados e uso de imagem)" in html


def test_criterio_4_problema_de_saude_aceita_descricao_sem_exigir_laudo(ambiente):
    cliente, sessoes, _ = ambiente

    aluno_id = cadastrar(cliente, sessoes, problema_saude="sim", descricao_saude="Asma")

    aluno = aluno_no_banco(sessoes, aluno_id)
    assert aluno.problema_saude
    assert aluno.descricao_saude == "Asma"
    assert aluno.documento("laudo") is None


def test_descricao_de_saude_e_ignorada_sem_problema_de_saude(ambiente):
    cliente, sessoes, _ = ambiente

    aluno_id = cadastrar(cliente, sessoes, problema_saude="nao", descricao_saude="Asma")

    assert aluno_no_banco(sessoes, aluno_id).descricao_saude is None


def test_criterio_5_cadastro_sem_documentos_e_aceito_com_pendencias(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    resposta = cliente.get(f"{BASE}/{aluno_id}")

    assert "5 documentos pendentes" in resposta.text
    for pendencia in ("Ficha assinada pelo responsável", "Foto 3x4", "Atestado para prática de esporte", "Comprovante de residência", "Certificado de graduação"):
        assert pendencia in resposta.text


def test_faixa_branca_nao_cobra_certificado(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes, graduacao="Branca")

    resposta = cliente.get(f"{BASE}/{aluno_id}")

    assert "4 documentos pendentes" in resposta.text
    assert "Não exigido na faixa branca" in resposta.text


def test_formato_de_arquivo_invalido_e_recusado(ambiente):
    cliente, sessoes, _ = ambiente
    nova_turma(cliente)

    resposta = cliente.post(
        f"{BASE}/novo",
        data=ficha(ids_das_turmas(sessoes)[0]),
        files={"doc_foto": ("foto.pdf", PDF, "application/pdf")},
    )

    assert resposta.status_code == 422
    assert "Envie foto do aluno em JPG, PNG ou WEBP." in resposta.text


# ---------- RNF12: dados de saúde e anexos cifrados ----------

def test_dados_de_saude_ficam_cifrados_no_banco(ambiente):
    cliente, sessoes, engine = ambiente
    aluno_id = cadastrar(cliente, sessoes, problema_saude="sim", descricao_saude="Asma severa", q2="sim", q2_qual="Asma")

    with engine.connect() as conexao:
        descricao, questionario = conexao.execute(
            text("SELECT descricao_saude, questionario FROM alunos WHERE id = :id"), {"id": aluno_id}
        ).one()

    assert "Asma" not in descricao
    assert "Asma" not in questionario
    assert aluno_no_banco(sessoes, aluno_id).respostas["q2"] == {"resposta": "sim", "qual": "Asma"}


def test_anexo_fica_cifrado_fora_da_pasta_publica_e_so_sai_pela_rota(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes, arquivos_enviados={"doc_laudo": ("laudo.pdf", PDF, "application/pdf")})
    documento = aluno_no_banco(sessoes, aluno_id).documento("laudo")

    gravado = (arquivos.DIRETORIO_ARQUIVOS / documento.caminho).read_bytes()
    assert PDF not in gravado

    resposta = cliente.get(f"{BASE}/{aluno_id}/documentos/{documento.id}?baixar=true")
    assert resposta.status_code == 200
    assert resposta.content == PDF
    assert resposta.headers["content-disposition"].startswith("attachment")


# ---------- RF23: consultar ficha ----------

def test_lista_mostra_alunos_e_contagem(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    resposta = cliente.get(BASE)

    assert resposta.status_code == 200
    assert "Ana Clara de Oliveira Santos" in resposta.text
    assert f"{BASE}/{aluno_id}" in resposta.text
    assert "1 ativo e 0 inativos" in resposta.text


def test_lista_busca_por_nome(ambiente):
    cliente, sessoes, _ = ambiente
    cadastrar(cliente, sessoes)

    assert "Ana Clara" in cliente.get(BASE, params={"busca": "clara"}).text
    assert "Nenhum aluno encontrado" in cliente.get(BASE, params={"busca": "Pedro"}).text


def test_criterio_1_ficha_exibe_dados_anexos_e_historico(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes, arquivos_enviados={"doc_foto": ("ana.png", PNG, "image/png")})

    resposta = cliente.get(f"{BASE}/{aluno_id}")

    html = resposta.text
    assert "Maria de Oliveira Santos" in html
    assert "ana.png" in html
    assert "Histórico de participação em turmas" in html
    assert "Vínculo atual" in html


def test_criterio_2_documento_anexado_pode_ser_baixado(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes, arquivos_enviados={"doc_foto": ("ana.png", PNG, "image/png")})
    foto = aluno_no_banco(sessoes, aluno_id).documento("foto")

    resposta = cliente.get(f"{BASE}/{aluno_id}/documentos/{foto.id}")

    assert resposta.status_code == 200
    assert resposta.content == PNG
    assert resposta.headers["content-type"] == "image/png"


def test_criterio_4_ficha_pode_ser_impressa(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    assert "data-imprimir" in cliente.get(f"{BASE}/{aluno_id}").text


# ---------- RF22: editar ficha ----------

def test_criterio_1_anexar_laudo_na_edicao(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes, problema_saude="sim")
    turma_id = ids_das_turmas(sessoes)[0]

    resposta = cliente.post(
        f"{BASE}/{aluno_id}/editar",
        data=ficha(turma_id, problema_saude="sim", termo_aceito=None),
        files={"doc_laudo": ("laudo.pdf", PDF, "application/pdf")},
    )

    assert resposta.status_code == 303
    assert aluno_no_banco(sessoes, aluno_id).documento("laudo").nome_original == "laudo.pdf"


def test_criterio_2_esvaziar_obrigatorio_na_edicao_bloqueia(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    resposta = cliente.post(f"{BASE}/{aluno_id}/editar", data=ficha(ids_das_turmas(sessoes)[0], telefone_mae=""))

    assert resposta.status_code == 422
    assert "Alterações ainda não salvas" in resposta.text
    assert aluno_no_banco(sessoes, aluno_id).telefone_mae == "(61) 99999-0102"


def test_criterio_3_trocar_turma_preserva_o_historico(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)
    nova_turma(cliente, modalidade="Capoeira", dias=("sabado",))
    judo, capoeira = ids_das_turmas(sessoes)

    resposta = cliente.post(f"{BASE}/{aluno_id}/editar", data=ficha(capoeira))

    assert resposta.status_code == 303
    aluno = aluno_no_banco(sessoes, aluno_id)
    assert aluno.vinculo_atual.turma_id == capoeira
    [anterior] = [a for a in aluno.associacoes if a.turma_id == judo]
    assert anterior.fim is not None
    assert "Ana Clara" not in cliente.get(f"/coordenacao/turmas/{judo}/alunos").text
    assert "Ana Clara" in cliente.get(f"/coordenacao/turmas/{capoeira}/alunos").text


def test_formulario_de_edicao_vem_preenchido(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    resposta = cliente.get(f"{BASE}/{aluno_id}/editar")

    assert 'value="Maria de Oliveira Santos"' in resposta.text
    assert "Termo aceito em" in resposta.text


# ---------- RF24: inativar aluno ----------

def test_confirmacao_antes_de_inativar(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    resposta = cliente.get(f"{BASE}/{aluno_id}/inativar")

    assert "Deseja inativar Ana Clara de Oliveira Santos?" in resposta.text
    assert aluno_no_banco(sessoes, aluno_id).ativo


def test_criterio_1_e_3_inativar_preserva_dados_e_mostra_a_data(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    resposta = cliente.post(f"{BASE}/{aluno_id}/inativar")

    assert resposta.status_code == 303
    assert resposta.headers["location"].endswith(f"{BASE}/{aluno_id}?aviso=inativado")
    aluno = aluno_no_banco(sessoes, aluno_id)
    assert not aluno.ativo
    assert aluno.inativado_em is not None
    assert aluno.nome_mae == "Maria de Oliveira Santos"
    assert aluno.vinculo_atual is not None

    ficha_html = cliente.get(f"{BASE}/{aluno_id}?aviso=inativado").text
    assert "Aluno inativado." in ficha_html
    assert f"Inativado em {aluno.inativado_em.strftime('%d/%m/%Y')}" in ficha_html
    assert "0 ativos e 1 inativo" in cliente.get(BASE).text


def test_criterio_2_cancelar_nao_muda_o_status(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)

    pagina = cliente.get(f"{BASE}/{aluno_id}/inativar").text

    assert f'href="http://testserver{BASE}/{aluno_id}">Cancelar' in pagina
    assert aluno_no_banco(sessoes, aluno_id).ativo


def test_inativar_duas_vezes_retorna_409(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)
    cliente.post(f"{BASE}/{aluno_id}/inativar")

    assert cliente.post(f"{BASE}/{aluno_id}/inativar").status_code == 409


def test_aluno_inativo_continua_na_lista_da_turma(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)
    cliente.post(f"{BASE}/{aluno_id}/inativar")

    html = cliente.get(f"/coordenacao/turmas/{ids_das_turmas(sessoes)[0]}/alunos").text

    assert "Ana Clara de Oliveira Santos" in html
    assert "Inativo" in html


# ---------- RF06: associar aluno a partir da turma ----------

def test_criterio_3_associar_aluno_existente_pela_turma(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)
    nova_turma(cliente, modalidade="Capoeira", dias=("sabado",))
    capoeira = ids_das_turmas(sessoes)[1]

    pagina = cliente.get(f"/coordenacao/turmas/{capoeira}/alunos/associar").text
    assert f'<option value="{aluno_id}"' in pagina

    resposta = cliente.post(f"/coordenacao/turmas/{capoeira}/alunos", data={"aluno_id": str(aluno_id)})

    assert resposta.status_code == 303
    assert "Ana Clara de Oliveira Santos" in cliente.get(f"/coordenacao/turmas/{capoeira}/alunos").text
    assert aluno_no_banco(sessoes, aluno_id).vinculo_atual.turma_id == capoeira


def test_aluno_inativo_nao_e_associado(ambiente):
    cliente, sessoes, _ = ambiente
    aluno_id = cadastrar(cliente, sessoes)
    cliente.post(f"{BASE}/{aluno_id}/inativar")
    nova_turma(cliente, modalidade="Capoeira", dias=("sabado",))
    capoeira = ids_das_turmas(sessoes)[1]

    resposta = cliente.post(f"/coordenacao/turmas/{capoeira}/alunos", data={"aluno_id": str(aluno_id)})

    assert resposta.status_code == 409


# ---------- Rotas ----------

@pytest.mark.parametrize("caminho", ["/99", "/99/editar", "/99/inativar", "/99/documentos/1"])
def test_aluno_inexistente_retorna_404(ambiente, caminho):
    cliente, _, _ = ambiente

    assert cliente.get(f"{BASE}{caminho}").status_code == 404


@pytest.mark.parametrize("caminho", ["", "/novo", "/1", "/1/editar", "/1/inativar", "/1/documentos/1"])
def test_rotas_exigem_login(ambiente, caminho):
    cliente, _, _ = ambiente
    del app.dependency_overrides[exigir_admin]

    resposta = cliente.get(f"{BASE}{caminho}")

    assert resposta.status_code in (302, 303, 401)


def test_lista_de_turmas_conta_os_alunos_atuais(ambiente):
    cliente, sessoes, _ = ambiente
    cadastrar(cliente, sessoes)

    html = cliente.get("/coordenacao/turmas").text

    assert "1 aluno associado" in html
    assert "1 aluno</span>" in html.replace("\n", "")
