from sqlalchemy import Column, Integer, String, Float, DateTime, func
from .database import Base
# Definir tabelas
class Producao(Base):
    __tablename__ = "producao"

    ano = Column(Integer, primary_key = True)
    categoria = Column(String(450), primary_key = True)
    produto = Column(String(450), primary_key = True)
    quantidade = Column(Float)

class Processamento(Base):
    __tablename__ = "processamento"

    ano = Column(Integer, primary_key = True)
    subopcao = Column(String(450), primary_key = True)
    categoria = Column(String(450), primary_key = True)
    produto = Column(String(450), primary_key = True)
    quantidade = Column(Float)

class Comercializacao(Base):
    __tablename__ = "comercializacao"

    ano = Column(Integer, primary_key = True)
    categoria = Column(String(450), primary_key = True)
    produto = Column(String(450), primary_key = True)
    quantidade = Column(Float)

class Importacao(Base):
    __tablename__ = "importacao"

    ano = Column(Integer, primary_key = True)
    subopcao = Column(String(450), primary_key = True)
    pais = Column(String(450), primary_key = True)
    quantidade = Column(Float)
    valor = Column(Float)

class Exportacao(Base):
    __tablename__ = "exportacao"

    ano = Column(Integer, primary_key = True)
    subopcao = Column(String(450), primary_key = True)
    pais = Column(String(450), primary_key = True)
    quantidade = Column(Float)
    valor = Column(Float)

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True, primary_key=True)
    username = Column(String(50), unique=True)
    password = Column(String(150))
    email = Column(String(150), unique=True)
    created_at = Column(DateTime, server_default=func.now())