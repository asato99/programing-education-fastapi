from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text, DateTime
from sqlalchemy.orm import sessionmaker

from datetime import datetime
from typing import Optional

Base = declarative_base()
class Problem(Base):
    __tablename__ = "problem"
    problem_cd = Column(String(30), primary_key=True)
    format = Column(Integer)
    title = Column(String(50))
    question = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )


dbname = 'tetdb'
user = 'sabira:okioki'
host = 'localhost:5432'
url = f"postgresql://{user}@{host}/{dbname}"

engine = create_engine(f"postgresql://{user}@{host}/{dbname}", echo=True)
def create_db_and_tables():
    Base.metadata.create_all(engine)

def get_engine():
    return engine

def get_session():
    SessionClass = sessionmaker(engine)
    return SessionClass()

if __name__ == '__main__':
    create_db_and_tables()