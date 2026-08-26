#Aqui vamos criar as dependencias que vamos usar no projeto, como o banco de dados e o motor de conexão com o banco de dados.
from sqlalchemy.orm import sessionmaker, Session
from models import db, Cliente
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM, oauth2_schema

def pegar_sessao_db():
    #Criar a sessão do banco de dados
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()

def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao_db)):
    try:
        dict_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
        email_usuario = dict_info.get("user_email")
    except JWTError:
        raise HTTPException(status_code= 401, detail="Acesso Negado")
    usuario = session.query(Cliente).filter(Cliente.email == email_usuario).first()
    if not usuario:
        raise HTTPException(status_code= 401, detail="Acesso Inválido")
    return usuario
