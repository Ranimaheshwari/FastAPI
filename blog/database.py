
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

sqlalchemy_db_URL = 'sqlite:///./New_blog.db'
# sqlalchemy_db_URL = "postgresql://postgres:rani1234@localhost:5432/db"


engine = create_engine(sqlalchemy_db_URL
,connect_args={"check_same_thread": False}
)

Session_local = sessionmaker(bind = engine,autocommit=False, autoflush=False)

Base = declarative_base()

def get_db():
    db = Session_local()
    try:
        yield db
    finally :
        db.close()