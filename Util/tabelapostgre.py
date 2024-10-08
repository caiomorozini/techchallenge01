from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
import sys
import os

# Adiciona o diretório 'Classes' ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Classes')))

from producaobase import Producao

# Configuração da conexão com o PostgreSQL
DATABASE_URL = "postgresql://postgres:fiap@localhost:5432/fiaptechchallenge01"

# Criação do engine
engine = create_engine(DATABASE_URL)

# Criação da sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

