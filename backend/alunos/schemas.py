"""Campos da ficha do aluno (RF21) e sua validação, com as mensagens mostradas no formulário."""
from dataclasses import dataclass
from datetime import date

# Questionário de prontidão para atividade física da ficha de papel do CECP (RN35)
QUESTOES = [
    ("q1", "Fez alguma avaliação médica antes de iniciar as atividades físicas?", False),
    ("q2", "Tem algum problema de saúde?", True),
    ("q3", "Sente dores no peito ao praticar atividades físicas?", False),
    ("q4", "Apresenta desequilíbrio por tontura ou perda momentânea da consciência?", False),
    ("q5", "Possui problema ósseo ou articular que pode ser agravado pela atividade física?", False),
    ("q6", "Faz uso de medicação contínua ou controlada?", True),
    ("q7", "Faz tratamento para pressão arterial ou problemas cardíacos?", True),
    ("q8", "Faz tratamento médico contínuo que possa ser afetado pela atividade física?", True),
    ("q9", "Já fez cirurgia que comprometa a atividade física?", True),
    ("q10", "Usa marca-passo, CDI ou outro aparelho cardíaco?", True),
    ("q11", "Sabe de outra razão pela qual a atividade física possa comprometer sua saúde?", True),
]

TIPOS_DOCUMENTO = {
    "foto": "Foto do aluno",
    "ficha_assinada": "Ficha assinada pelo responsável",
    "foto_3x4": "Foto 3x4",
    "atestado": "Atestado para prática de esporte",
    "comprovante_residencia": "Comprovante de residência",
    "certificado_graduacao": "Certificado de graduação",
    "laudo": "Laudo",
}

TIPOS_ARQUIVO_IMAGEM = {"image/jpeg", "image/png", "image/webp"}
# Documentos podem ser imagem digitalizada ou PDF (RN42)
TIPOS_ARQUIVO_DOCUMENTO = TIPOS_ARQUIVO_IMAGEM | {"application/pdf"}
TAMANHO_MAXIMO_ARQUIVO = 10 * 1024 * 1024

GRADUACOES = ["Branca", "Cinza", "Azul", "Amarela", "Laranja", "Verde", "Roxa", "Marrom", "Preta"]
TIPOS_ESCOLA = {"publica": "Pública", "particular": "Particular"}

CAMPOS_OBRIGATORIOS = {
    "nome": "Nome completo",
    "data_inicio": "Data de início",
    "documento_identificacao": "Documento de identificação",
    "nome_mae": "Nome da mãe",
    "telefone_mae": "Telefone da mãe",
    "celular": "Celular",
    "graduacao": "Graduação",
    # Quem dá o consentimento pelo aluno (LGPD, art. 14 §1)
    "responsavel_nome": "Nome do responsável legal",
}

# Versão do termo apresentado; fica gravada junto com o aceite (PEN14)
TERMO_VERSAO = "1.0-provisoria"

# Dados da ficha de papel que o protótipo de 10/11 trouxe como opcionais
CAMPOS_OPCIONAIS = [
    "cpf", "endereco", "cidade", "cep", "nome_pai", "telefone_pai", "telefone_residencial",
    "telefone_emergencia", "nome_contato_urgencia", "responsavel_cpf",
    "responsavel_identidade", "acompanhante", "nome_escola",
]
SAIDAS_ALUNO = {"sozinho": "Sozinho", "acompanhado": "Acompanhado"}
TURNOS = {"manha": "Manhã", "tarde": "Tarde", "noite": "Noite", "integral": "Integral"}


@dataclass
class FichaAluno:
    """Dados da ficha já validados, prontos para gravar."""

    campos: dict
    respostas: dict
    turma_id: int


def _data(texto: str, campo: str, rotulo: str, erros: dict) -> date | None:
    if not texto:
        return None
    try:
        return date.fromisoformat(texto)
    except ValueError:
        erros[campo] = f"Informe {rotulo} no formato dia/mês/ano."
        return None


def _opcao(formulario, campo: str, opcoes: dict) -> str | None:
    valor = formulario.get(campo) or ""
    return valor if valor in opcoes else None


def validar_ficha(formulario, exigir_termo: bool) -> tuple[FichaAluno | None, dict]:
    """Valida o formulário da ficha. Devolve os dados ou os erros por campo.

    Sem campo obrigatório, sem questionário completo (RN35) ou, no cadastro, sem o aceite do
    termo único (RN40), a ficha não é gravada. Documentos são opcionais (RN39).
    """
    erros: dict[str, str] = {}
    texto = {nome: (formulario.get(nome) or "").strip() for nome in [*CAMPOS_OBRIGATORIOS, *CAMPOS_OPCIONAIS]}

    for nome, rotulo in CAMPOS_OBRIGATORIOS.items():
        if not texto[nome]:
            erros[nome] = f"Preencha o campo {rotulo}. Se o dado não existir, escreva \"não aplicável\"."

    campos = {nome: texto[nome] for nome in CAMPOS_OBRIGATORIOS}
    campos |= {nome: texto[nome] or None for nome in CAMPOS_OPCIONAIS}
    campos["data_inicio"] = _data(texto["data_inicio"], "data_inicio", "a data de início", erros)
    campos["data_nascimento"] = _data(
        (formulario.get("data_nascimento") or "").strip(), "data_nascimento", "a data de nascimento", erros
    )
    campos["saida_aluno"] = _opcao(formulario, "saida_aluno", SAIDAS_ALUNO)
    campos["turno_escolar"] = _opcao(formulario, "turno_escolar", TURNOS)
    if campos["saida_aluno"] != "acompanhado":
        campos["acompanhante"] = None

    campos["tipo_escola"] = _opcao(formulario, "tipo_escola", TIPOS_ESCOLA)
    if campos["tipo_escola"] is None:
        erros["tipo_escola"] = "Informe se a escola é pública ou particular."

    problema_saude = formulario.get("problema_saude") or ""
    if problema_saude not in ("sim", "nao"):
        erros["problema_saude"] = "Informe se há problema de saúde ou necessidade especial."
    campos["problema_saude"] = problema_saude == "sim"
    # Descrição só quando há problema de saúde (RN38)
    campos["descricao_saude"] = (formulario.get("descricao_saude") or "").strip() or None if problema_saude == "sim" else None

    respostas = {}
    faltando = []
    for codigo, _, tem_qual in QUESTOES:
        resposta = formulario.get(codigo) or ""
        if resposta not in ("sim", "nao"):
            faltando.append(codigo[1:])
            continue
        qual = (formulario.get(f"{codigo}_qual") or "").strip() if tem_qual and resposta == "sim" else ""
        respostas[codigo] = {"resposta": resposta, "qual": qual}
    if faltando:
        erros["questionario"] = (
            "Responda todas as perguntas do questionário para liberar o cadastro. Faltam: "
            + ", ".join(faltando) + "."
        )

    turma = (formulario.get("turma_id") or "").strip()
    if not turma.isdigit():
        erros["turma_id"] = "Escolha a turma: modalidade, dias e horário fazem parte da ficha."

    # Termo único (RN40, DEC25): um aceite obrigatório cobre responsabilidade, dados (inclusive de saúde)
    # e uso de imagem. A recusa impede o cadastro, como na RN16; o termo informa isso em destaque (LGPD, art. 9º §3)
    if exigir_termo and formulario.get("termo_aceito") != "sim":
        erros["termo_aceito"] = "O cadastro só é concluído com o aceite do termo de responsabilidade, dados e uso de imagem."

    if erros:
        return None, erros
    return FichaAluno(campos=campos, respostas=respostas, turma_id=int(turma)), {}
