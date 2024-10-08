# Classes/producaobase.py
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

# Criação da base para as classes do SQLAlchemy
Base = declarative_base()

# Definição da classe Producao
class Producao(Base):
    __tablename__ = "producao"
    id = Column(Integer, primary_key=True, index=True)
    nome_produto = Column(String, index=True)
    quantidade = Column(Float)
    ano = Column(Integer)