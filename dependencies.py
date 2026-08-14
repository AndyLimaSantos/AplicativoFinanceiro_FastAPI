#Aqui vamos criar as dependencias que vamos usar no projeto, como o banco de dados e o motor de conexão com o banco de dados.
from sqlalchemy.orm import sessionmaker
from models import db

def pegar_sessao_db():
    #Criar a sessão do banco de dados
    try:
        Session = sessionmaker(bind=db)
        session = Session()
        yield session
    finally:
        session.close()