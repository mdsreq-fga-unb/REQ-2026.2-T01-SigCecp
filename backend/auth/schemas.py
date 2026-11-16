from pydantic import BaseModel


class LoginForm(BaseModel):

    usuario: str
    senha: str
