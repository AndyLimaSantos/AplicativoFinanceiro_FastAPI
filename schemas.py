#arquivo responsavel por fazer a tipagem dos dados, facilçitando assim o processo de validação e documentação da API.
from pydantic import BaseModel, Field
from typing import Optional


class ClienteSchemas(BaseModel):
    nome: str
    email: str
    senha: str

    class Config:
        from_attributes = True  

class LoginSchemas(BaseModel):
    email: str
    senha: str
    class Config:
        from_attributes = True