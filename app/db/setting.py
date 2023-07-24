from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from config import database

Base = declarative_base()

dbname = database.DB_NAME
user = f"{database.DB_USER}:{database.DB_PASSWORD}"
host = f"{database.DB_HOST}:{database.DB_PORT}"
url = f"postgresql://{user}@{host}/{dbname}"
engine = create_engine(f"postgresql://{user}@{host}/{dbname}", echo=True)

def create_db_and_tables():
    Base.metadata.create_all(engine)

def get_session():
    SessionClass = sessionmaker(engine)
    return SessionClass()

if __name__ == '__main__':
    create_db_and_tables()