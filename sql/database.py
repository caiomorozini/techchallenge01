from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .connection_string import con_str
from tenacity import retry, stop_after_attempt, wait_exponential


connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": con_str})
engine = create_engine(connection_url, use_setinputsizes = False, echo = False, fast_executemany = True, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=60))
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
