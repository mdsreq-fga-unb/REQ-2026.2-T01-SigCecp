from typing import Literal, Self
from pydantic import BaseModel, Field, ValidationInfo, field_validator, model_validator


class PublicacaoCreate(BaseModel):
    titulo: str = Field(max_length=120)
    descricao: str = Field(max_length=16000) 
    
    

    @field_validator("*", mode="before")
    @classmethod
    def remover_espacos_externos(cls, valor: object) -> object:
        if isinstance(valor, str):
            return valor.strip()
        return valor

    @field_validator("titulo")
    @classmethod
    def validar_texto_obrigatorio(cls, valor: str, info: ValidationInfo) -> str:
        if not valor:
            raise ValueError(f"O campo {info.field_name} deve ser preenchido.")
        return valor


    

    

   