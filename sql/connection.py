from sqlalchemy import MetaData, Table, Column, Integer, String, Float, DateTime
from database import engine

# Definir metadados
metadata = MetaData()

# Definir tabelas
producao = Table('Producao', metadata,
    Column('ano', Integer),
    Column('categoria', String(50)),
    Column('produto', String(50)),
    Column('quantidade', Float)
)

processamento = Table('Processamento', metadata,
    Column('ano', Integer),
    Column('subopcao', String(50)),
    Column('categoria', String(50)),
    Column('produto', String(50)),
    Column('quantidade', Float)
)

comercializacao = Table('Comercializacao', metadata,
    Column('ano', Integer),
    Column('categoria', String(50)),
    Column('produto', String(50)),
    Column('quantidade', Float)
)

importacao = Table('Importacao', metadata,
    Column('ano', Integer),
    Column('subopcao', String(50)),
    Column('pais', String(50)),
    Column('quantidade', Float),
    Column('valor', Float)
)

exportacao = Table('Exportacao', metadata,
    Column('ano', Integer),
    Column('subopcao', String(50)),
    Column('pais', String(50)),
    Column('quantidade', Float),
    Column('valor', Float)
)

users = Table('users', metadata,
    Column('id', Integer),
    Column('username', String(50)),
    Column('password', String(150)),
    Column('email', String(150)),
    Column('created_at', DateTime)
)

# Criar as tabelas no banco de dados
metadata.create_all(engine, checkfirst=True)