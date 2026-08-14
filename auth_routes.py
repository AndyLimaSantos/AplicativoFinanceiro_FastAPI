from fastapi import APIRouter, HTTPException, Depends
from models import Cliente, db
#devemos importar o sqlalchemy e as sessões para edição no banco de dados, pois toda sessão de anco de dados deve ser encerrada e fazemos isso usando o Depends
from dependencies import pegar_sessao_db
from main import bcrypt_context
from schemas import ClienteSchemas






#CRIAÇÃO DA ROTA DE AUTENTIFICAÇÃO
auth_router = APIRouter(prefix="/auth", tags=["auth"])


#Criação
@auth_router.get("/")
async def auth():
    return {"message": "Rota de autenticação funcionando!"} 


@auth_router.post("/criar_usuario") #Criar um novo úsuario no sistema.
async def Criar_Usuario(cliente: ClienteSchemas, session=Depends(pegar_sessao_db)):
    #Verificar se o email já existe no banco de dados
    cliente_existente = session.query(Cliente).filter(Cliente.email == cliente.email).first()
    if cliente_existente:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    else:
        senha_criptografada = bcrypt_context.hash(cliente.senha)
        novo_cliente = Cliente(nome=cliente.nome, email=cliente.email, senha=senha_criptografada)
        session.add(novo_cliente)
        session.commit()
        return {"message": "Usuário criado com sucesso!"}