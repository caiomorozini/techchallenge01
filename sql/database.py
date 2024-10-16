from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from connection_string import con_str

connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": con_str})
engine = create_engine(con_str, use_setinputsizes = False, echo = False, fast_executemany = True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()