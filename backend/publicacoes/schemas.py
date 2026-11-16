
from pydantic import BaseModel, Field, field_validator


class PublicacaoCreate(BaseModel):
    titulo: str = Field(max_length=200)
    texto: str | None = Field(default=None, max_length=16000)

    @field_validator("*", mode="before")
    @classmethod
    def remover_espacos_externos(cls, valor):
        if isinstance(valor, str):
            return valor.strip()
        return valor

    @field_validator("titulo")
    @classmethod
    def validar_titulo(cls, valor: str) -> str:
        if not valor:
            raise ValueError("O título deve ser preenchido.")
        return valor
