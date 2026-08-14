from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
SECERET_KEY = os.getenv("SECRET_KEY")  # Obtém a chave secreta do arquivo .env

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
from auth_routes import auth_router

#INCLUSÃO DAS ROTAS
#---------------------------------------------

#INCLUSÃO DA ROTA DE AUTENTIFICAÇÃO NO SISTEMA
app.include_router(auth_router)