from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from dotenv import load_dotenv

import os

load_dotenv()  # Carrega as variáveis de ambiente do arquivo .env
SECRET_KEY = os.getenv("SECRET_KEY")  # Obtém a chave secreta do arquivo .env
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
ALGORITHM = os.getenv("ALGORITHM")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema  = OAuth2PasswordBearer(tokenUrl = "auth/login-form")

from auth_routes import auth_router
from store_routes import store_router

#INCLUSÃO DAS ROTAS
#---------------------------------------------

#INCLUSÃO DA ROTA DE AUTENTIFICAÇÃO NO SISTEMA
app.include_router(auth_router)
app.include_router(store_router)