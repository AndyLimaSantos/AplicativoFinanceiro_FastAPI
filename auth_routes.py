from fastapi import APIRouter, HTTPException, Depends
from models import Cliente, db
#devemos importar o sqlalchemy e as sessões para edição no banco de dados, pois toda sessão de anco de dados deve ser encerrada e fazemos isso usando o Depends
from dependencies import pegar_sessao_db
from main import bcrypt_context, ACCESS_TOKEN_EXPIRE_MINUTES,SECRET_KEY, ALGORITHM
from schemas import ClienteSchemas, LoginSchemas
from sqlalchemy.orm import Session, sessionmaker
from datetime import datetime, timezone, timedelta
from jose import jwt, JWTError


#CRIAÇÃO DA ROTA DE AUTENTIFICAÇÃO
auth_router = APIRouter(prefix="/auth", tags=["auth"])


def autentificar_usuario(email, senha, session):
    usuario = session.query(Cliente).filter(Cliente.email == email).first()
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    return usuario

def criar_token(email, duaracao_token = timedelta(minutes= ACCESS_TOKEN_EXPIRE_MINUTES)):
    data_expiracao = datetime.now(timezone.utc) + duaracao_token
    dict_info = {"user_email":email, "exp": data_expiracao}
    encode_jwt = jwt.encode(dict_info, SECRET_KEY, ALGORITHM)
    return encode_jwt

def verifica_token(token, session):
    usuario = session.query(Cliente).filter(Cliente.id == 1).first()
    return usuario





#Criação
@auth_router.get("/")
async def auth():
    return {"message": "Rota de autenticação funcionando!"} 


@auth_router.post("/criar_usuario") #Criar um novo úsuario no sistema.
async def Criar_Usuario(cliente: ClienteSchemas, session: Session = Depends(pegar_sessao_db)):
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


@auth_router.post("/login")
async def Login(login_schemas : LoginSchemas, session: Session = Depends(pegar_sessao_db)):
    #o Login precisa de email e senha para verificar a validade do úsuario
    #Para ocorrer a verificação iremos criptografar toda senha inserida pelo
    #úsuario e comparar com a senha  inserida no banco de dados
    #precisamos de um loginschemas que vai conter as informações que precisam paa o login
    usuario = autentificar_usuario(login_schemas.email, login_schemas.senha, session)
    if not usuario:
        raise HTTPException(status_code = 400, detail="Úsuario não encontrado ou cedeênciais invalída")
    else:
        #criar um token para o úsuario utilizar nas outras partes do istema e poder continuar com o acesso sem precisar sair.
        access_token = criar_token(login_schemas.email)
        refresh_token = criar_token(login_schemas.email, timedelta(days = 7))
        return {"access_token":access_token,\
                "refresh_token":refresh_token,\
                "token_type":"Bearer"}

@auth_router.get("/refresh")
async def use_refresh_token(token, session: Session = Depends(pegar_sessao_db)):
    usuario = verifica_token(token, session)
    access_token = criar_token(usuario.email)
    return {"access_token":access_token,\
            "token_type":"Bearer"
            }
