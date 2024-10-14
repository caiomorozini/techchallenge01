from sqlalchemy import Column, Integer, String, Float
from .database import Base

# Definir tabelas
class Producao(Base):
    __tablename__ = "producao"

    ano = Column(Integer, primary_key = True)
    categoria = Column(String, primary_key = True)
    produto = Column(String, primary_key = True)
    quantidade = Column(Float)

class Processamento(Base):
    __tablename__ = "processamento"

    ano = Column(Integer, primary_key = True)
    subopcao = Column(String, primary_key = True)
    categoria = Column(String, primary_key = True)
    produto = Column(String, primary_key = True)
    quantidade = Column(Float)

class Comercializacao(Base):
    __tablename__ = "comercializacao"

    ano = Column(Integer, primary_key = True)
    categoria = Column(String, primary_key = True)
    produto = Column(String, primary_key = True)
    quantidade = Column(Float)

class Importacao(Base):
    __tablename__ = "importacao"

    ano = Column(Integer, primary_key = True)
    subopcao = Column(String, primary_key = True)
    pais = Column(String, primary_key = True)
    quantidade = Column(Float)
    valor = Column(Float)

class Exportacao(Base):
    __tablename__ = "exportacao"

    ano = Column(Integer, primary_key = True)
    subopcao = Column(String, primary_key = True)
    pais = Column(String, primary_key = True)
    quantidade = Column(Float),
    valor = Column(Float)