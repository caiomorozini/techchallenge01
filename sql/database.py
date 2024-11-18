from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sql.connection_string import con_str
from tenacity import retry, stop_after_attempt, wait_exponential, RetryError

# connection_url = URL.create("postgresql+psycopg2", query={"odbc_connect": con_str})
engine = create_engine(con_str, echo = False, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@retry(stop=stop_after_attempt(5), wait=wait_exponential(multiplier=1, max=60),retry_error_cls=RetryError)
def bindEngine():
    Base.metadata.create_all(bind=engine)
