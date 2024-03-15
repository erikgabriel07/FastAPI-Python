from pydantic import BaseModel


class Model(BaseModel):
    nome: str
    idade: int
    email: str
    endereco: str
    telefone: int
