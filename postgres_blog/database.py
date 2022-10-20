
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


sqlalchemy_db_URL = "postgresql://postgres:rani1234@localhost:5432/Blog_Postgres"


engine = create_engine(sqlalchemy_db_URL, pool_size=20, max_overflow=0)

Session_local = sessionmaker(bind = engine,autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally :
        db.close()