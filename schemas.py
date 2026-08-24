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

class CriarIntegracaoSchemas(BaseModel):
    plataforma: str #MERCADO LIVRE, SHOPEE, TIKTOK SHOP, SHEIN, no front end colocar essas informações de selecionar, não deixar o usuario escrver 
    nome_loja: str 
    fuso_horario: str 
    moeda: str #Talvez aqui no fronto end coloca as opções que devem ser inseridos o sistema 
    url_loja: str #Não sei como vou fazer isso haha
    api_key: str #Não sei como vou fazer isso haha
    class Config:
        from_attributes = True