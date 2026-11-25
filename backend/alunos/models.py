import json
from datetime import date, datetime

from sqlalchemy import Boolean, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.cripto import TextoCifrado
from backend.database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(200), nullable=False)
    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    documento_identificacao: Mapped[str] = mapped_column(String(60), nullable=False)
    nome_mae: Mapped[str] = mapped_column(String(200), nullable=False)
    telefone_mae: Mapped[str] = mapped_column(String(30), nullable=False)
    telefone_pai: Mapped[str | None] = mapped_column(String(30))
    celular: Mapped[str] = mapped_column(String(30), nullable=False)
    telefone_emergencia: Mapped[str | None] = mapped_column(String(30))
    tipo_escola: Mapped[str] = mapped_column(String(20), nullable=False)
    nome_escola: Mapped[str | None] = mapped_column(String(200))
    graduacao: Mapped[str] = mapped_column(String(60), nullable=False)

    # Dados opcionais da ficha de papel
    data_nascimento: Mapped[date | None] = mapped_column(Date)
    cpf: Mapped[str | None] = mapped_column(String(20))
    endereco: Mapped[str | None] = mapped_column(String(255))
    cidade: Mapped[str | None] = mapped_column(String(100))
    cep: Mapped[str | None] = mapped_column(String(15))
    nome_pai: Mapped[str | None] = mapped_column(String(200))
    telefone_residencial: Mapped[str | None] = mapped_column(String(30))
    nome_contato_urgencia: Mapped[str | None] = mapped_column(String(200))
    responsavel_nome: Mapped[str | None] = mapped_column(String(200))
    responsavel_cpf: Mapped[str | None] = mapped_column(String(20))
    responsavel_identidade: Mapped[str | None] = mapped_column(String(60))
    saida_aluno: Mapped[str | None] = mapped_column(String(20))
    acompanhante: Mapped[str | None] = mapped_column(String(200))
    turno_escolar: Mapped[str | None] = mapped_column(String(20))

    # Dados de saúde: cifrados no banco (RNF12)
    problema_saude: Mapped[bool] = mapped_column(Boolean, nullable=False)
    descricao_saude: Mapped[str | None] = mapped_column(TextoCifrado)
    questionario: Mapped[str] = mapped_column(TextoCifrado, nullable=False)

    # Prova do aceite do termo único (LGPD, art. 8º §2): data, versão do termo e responsável que aceitou
    # (nome e CPF do responsável legal, nos campos acima).
    termo_aceito_em: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    termo_versao: Mapped[str] = mapped_column(String(20), nullable=False)

    ativo: Mapped[bool] = mapped_column(Boolean, nullable=False, default=True)
    inativado_em: Mapped[datetime | None] = mapped_column(DateTime)
    criado_em: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    atualizado_em: Mapped[datetime | None] = mapped_column(DateTime)

    associacoes: Mapped[list["AlunoTurma"]] = relationship(
        back_populates="aluno", order_by="AlunoTurma.inicio", cascade="all, delete-orphan"
    )
    documentos: Mapped[list["AlunoDocumento"]] = relationship(
        back_populates="aluno", order_by="AlunoDocumento.enviado_em", cascade="all, delete-orphan"
    )

    @property
    def respostas(self) -> dict:
        return json.loads(self.questionario)

    @property
    def vinculos(self) -> list["AlunoTurma"]:
        """Associações cuja turma ainda existe. Turmas removidas antes da limpeza das associações são ignoradas."""
        return [a for a in self.associacoes if a.turma is not None]

    @property
    def turmas_atuais(self) -> list["AlunoTurma"]:
        return [a for a in self.vinculos if a.fim is None]

    @property
    def vinculo_atual(self) -> "AlunoTurma | None":
        atuais = self.turmas_atuais
        return atuais[-1] if atuais else None

    @property
    def ultimo_vinculo(self) -> "AlunoTurma | None":
        return self.vinculos[-1] if self.vinculos else None

    def documento(self, tipo: str) -> "AlunoDocumento | None":
        """Documento mais recente do tipo, ou None."""
        do_tipo = [d for d in self.documentos if d.tipo == tipo]
        return do_tipo[-1] if do_tipo else None


class AlunoTurma(Base):
    """Associação do aluno à turma. Retirar ou trocar a turma encerra a associação (DEC35)."""

    __tablename__ = "aluno_turmas"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    aluno_id: Mapped[int] = mapped_column(ForeignKey("alunos.id"), nullable=False, index=True)
    turma_id: Mapped[int] = mapped_column(ForeignKey("turmas.id"), nullable=False, index=True)
    inicio: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    fim: Mapped[datetime | None] = mapped_column(DateTime)

    aluno: Mapped[Aluno] = relationship(back_populates="associacoes")
    turma = relationship("Turma")


class AlunoDocumento(Base):
    """Anexo do aluno. O arquivo fica cifrado fora da pasta pública de mídias (RNF12)."""

    __tablename__ = "aluno_documentos"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    aluno_id: Mapped[int] = mapped_column(ForeignKey("alunos.id"), nullable=False, index=True)
    tipo: Mapped[str] = mapped_column(String(40), nullable=False)
    nome_original: Mapped[str] = mapped_column(String(255), nullable=False)
    caminho: Mapped[str] = mapped_column(String(255), nullable=False)
    content_type: Mapped[str] = mapped_column(String(100), nullable=False)
    enviado_em: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    aluno: Mapped[Aluno] = relationship(back_populates="documentos")
