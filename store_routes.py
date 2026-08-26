from fastapi import APIRouter, Depends, HTTPException
from models import Integracoes_Loja, Cliente
from dependencies import pegar_sessao_db, verificar_token
from sqlalchemy.orm import Session
from schemas import CriarIntegracaoSchemas

#Aqui tem as configurações de adicionar e verificar as lojas que já estão inseridas no sistema do Úsuario.
#OBJETIVOS
# Cada loja só poode ser inserida uma vêz
# Cada Loja tem suas informaçõles baseadas no banco de dados de integração
# algumas opções só serão efinidas pelo front-end, não serão inseridas pelo úsuario....
#
#    plataforma: str #MERCADO LIVRE, SHOPEE, TIKTOK SHOP, SHEIN, no front end colocar essas informações de selecionar, não deixar o usuario escrver 
#    nome_loja: str 
#    fuso_horario: str 
#    moeda: str #Talvez aqui no fronto end coloca as opções que devem ser inseridos o sistema 
#    url_loja: str #Não sei como vou fazer isso haha
#    api_key: str #Não sei como vou fazer isso haha




store_router = APIRouter(prefix="/store", tags=["store"], dependencies=[Depends(verificar_token)])

@store_router.post("/criar-integracao")
async def criar_integracao(cria_integracao: CriarIntegracaoSchemas, session: Session = Depends(pegar_sessao_db)):
    return {"message": "Integração criada com sucesso!"}

@store_router.post("/erase-integracao")
async def apagar_integracao(integracao_id: int, session: Session = Depends(pegar_sessao_db)):
    return {"message": "Integração apagada com sucesso!"}