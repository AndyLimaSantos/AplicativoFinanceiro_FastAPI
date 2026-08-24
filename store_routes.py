from fastapi import APIRouter, Depends
from models import Integracoes_Loja
from dependencies import pegar_sessao_db
from sqlalchemy.orm import Session
from schemas import CriarIntegracaoSchemas

store_router = APIRouter(prefix="/store", tags=["store"])

@store_router.post("/criar-integracao")
async def criar_integracao(cria_integracao: CriarIntegracaoSchemas, session: Session = Depends(pegar_sessao_db)):
    return {"message": "Integração criada com sucesso!"}

@store_router.post("/erase-integracao")
async def apagar_integracao(integracao_id: int, session: Session = Depends(pegar_sessao_db)):
    return {"message": "Integração apagada com sucesso!"}