from sqlalchemy import create_engine, Column, Integer, String, Integer, ForeignKey, Boolean, Float, DateTime
from sqlalchemy.orm import declarative_base

#Criar a conexão com o banco de dados
db = create_engine("sqlite:///banco.db")
#Criamos a base
Base = declarative_base()
#Criaremos as classes com as planilhas com elementos necessários para o banco de dados
class Cliente(Base):
    __tablename__ = "clientes"
    id = Column("id",Integer, primary_key=True, autoincrement=True)
    nome = Column("nome",String, nullable=False)
    email = Column("email",String, nullable=False)
    senha = Column("senha",String, nullable=False)

    def __init__(self, nome,email,senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Integracoes_Loja(Base):
    __tablename__ = "integracoes_loja"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    usuario_id = Column("usuario_id",Integer, ForeignKey("clientes.id"), nullable=False)
    plataforma = Column("plataforma",String, nullable=False)
    nome_loja = Column("nome_loja",String, nullable=False)
    fuso_horario = Column("fuso_horario",String, nullable=False)
    moeda = Column("moeda",String, nullable=False)
    url_loja = Column("url_loja",String, nullable=False)
    api_key = Column("api_key",String, nullable=False)

    def __init__(self, usuario_id, plataforma, url_loja, api_key):
        self.usuario_id = usuario_id
        self.plataforma = plataforma
        self.url_loja = url_loja
        self.api_key = api_key

class Assinatura(Base):
    __tablename__ = "assinaturas"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    usuario_id = Column("usuario_id",Integer, ForeignKey("clientes.id"), nullable=False)
    tipo_plano = Column("tipo_plano",String, nullable=False) #quantos planos vamos ter e oque vai ter em cada plano.
    status_conta = Column("status_conta",String, nullable=False)
    data_inicio = Column("data_inicio",DateTime, nullable=False)
    data_fim = Column("data_fim",DateTime, nullable=False)

    def __init__(self, usuario_id, tipo_plano, status_conta, data_inicio, data_fim):
        self.usuario_id = usuario_id
        self.tipo_plano = tipo_plano
        self.status_conta = status_conta
        self.data_inicio = data_inicio
        self.data_fim = data_fim

class Pedidos(Base):
    __tablename__ = "pedidos"

    id = Column("id",Integer, primary_key=True, autoincrement=True)
    integracao_loja_id = Column("integracao_loja_id",Integer, ForeignKey("integracoes_loja.id"), nullable=False)
    id_pedido_loja = Column("id_pedido_loja",String, nullable=False)
    valor_bruto = Column("valor_bruto",Float, nullable=False)
    custo_taxa = Column("custo_taxa",Float, nullable=False)
    data_venda = Column("data_venda",DateTime, nullable=False)
    status_pedido = Column("status_pedido",String, nullable=False)

    def __init__(self, integracao_loja_id, id_pedido_loja, valor_bruto, custo_taxa, data_venda, status_pedido):
        self.integracao_loja_id = integracao_loja_id
        self.id_pedido_loja = id_pedido_loja
        self.valor_bruto = valor_bruto
        self.custo_taxa = custo_taxa
        self.data_venda = data_venda
        self.status_pedido = status_pedido