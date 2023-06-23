from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

dbname = 'tetdb'
user = 'sabira:okioki'
host = 'localhost:5432'
url = f"postgresql://{user}@{host}/{dbname}"
engine = create_engine(f"postgresql://{user}@{host}/{dbname}", echo=True)

def create_db_and_tables():
    Base.metadata.create_all(engine)

def get_session():
    SessionClass = sessionmaker(engine)
    return SessionClass()

if __name__ == '__main__':
    create_db_and_tables()