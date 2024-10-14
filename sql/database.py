from sqlalchemy import URL, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

server = "techchallenge.database.windows.net"
database = "SQL_FIAP"
user = "azuredbbase"
password = "TechChallenge@321"

#driver = "SQL Server"
driver = "ODBC Driver 18 for SQL Server"
        
connection_string = f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={user};PWD={password}'
connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
engine = create_engine(connection_url, use_setinputsizes = False, echo = False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()