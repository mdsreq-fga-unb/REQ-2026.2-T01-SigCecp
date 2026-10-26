from datetime import date, time
from decimal import Decimal
from typing import Literal, Self

from pydantic import BaseModel, Field, ValidationInfo, field_validator, model_validator


class EventoCreate(BaseModel):
    titulo: str
    subtitulo: str
    nome: str
    data: date
    inicio: time
    termino: time
    local: str
    descricao: str
    alimentacao: bool
    pesagem: Literal["sim", "nao", "nao_se_aplica"]
    cobrado: bool
    valor: Decimal | None = Field(default=None, allow_inf_nan=False)
    data_limite_pagamento: date | None = None
    meio_pagamento: str | None = None

    @field_validator("*", mode="before")
    @classmethod
    def remover_espacos_externos(cls, valor: object) -> object:
        if isinstance(valor, str):
            return valor.strip()
        return valor

    @field_validator("titulo", "subtitulo", "nome", "local", "descricao")
    @classmethod
    def validar_texto_obrigatorio(cls, valor: str, info: ValidationInfo) -> str:
        if not valor:
            raise ValueError(f"O campo {info.field_name} deve ser preenchido.")
        return valor

    @field_validator("meio_pagamento")
    @classmethod
    def normalizar_meio_pagamento(cls, valor: str | None) -> str | None:
        return valor or None

    @model_validator(mode="after")
    def validar_pagamento(self) -> Self:
        if self.cobrado:
            if self.valor is None:
                raise ValueError("Informe o valor para eventos cobrados.")
            if self.data_limite_pagamento is None:
                raise ValueError("Informe a data limite de pagamento para eventos cobrados.")
            if self.meio_pagamento is None:
                raise ValueError("Informe o meio de pagamento para eventos cobrados.")
        return self
