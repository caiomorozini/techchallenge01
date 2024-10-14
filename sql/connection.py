from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float

# Nova string de conexão
connection_string = (
    'mssql+pyodbc://azuredbbase:TechChallenge@321@tcp:techchallenge.database.windows.net,1433/SQL_FIAP'
    '?driver=ODBC+Driver+18+for+SQL+Server&Encrypt=yes&TrustServerCertificate=no&Connection+Timeout=30'
)

# Criar o engine do SQLAlchemy
engine = create_engine(connection_string)

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

# Criar as tabelas no banco de dados
metadata.create_all(engine, checkfirst=True)