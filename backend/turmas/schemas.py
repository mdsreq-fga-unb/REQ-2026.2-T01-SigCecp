from datetime import date, time
from decimal import Decimal
from typing import Literal, Self

from pydantic import BaseModel, Field, ValidationInfo, field_validator, model_validator

DiaSemana = Literal[
    "segunda", "terca", "quarta", "quinta", "sexta", "sabado", "domingo"
]

class TurmaCreate(BaseModel):
    modalidade: str = Field(max_length=120)
    dias: list[DiaSemana] = Field(min_length=1)
    inicio: time
    termino: time
    alunos: list[str] = Field(default_factory=list)
    # Mantenha os validadores e o model_validator existentes.

    @field_validator("modalidade")
    @classmethod
    def validar_texto_obrigatorio(cls, valor: str, info: ValidationInfo) -> str:
        if not valor:
            raise ValueError(f"O campo {info.field_name} deve ser preenchido.")
        return valor

    @field_validator("inicio", "termino")
    @classmethod
    def validar_horario_local(cls, valor: time) -> time:
        if valor.tzinfo is not None:
            raise ValueError("Informe o horário local sem informação de fuso.")
        if valor.microsecond:
            raise ValueError("Informe o horário com precisão de segundos, sem frações.")
        return valor
