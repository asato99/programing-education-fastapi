from sqlmodel import Field, SQLModel, create_engine

from datetime import datetime
from typing import Optional

class Problem(SQLModel, table=True):
    problem_cd: str = Field(primary_key=True)
    format: int
    title: str
    question: str
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
    updated_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)


dbname = 'tetdb'
user = 'sabira:okioki'
host = 'localhost:5432'
url = f"postgresql://{user}@{host}/{dbname}"

engine = create_engine(f"postgresql://{user}@{host}/{dbname}", echo=True)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_engine():
    return engine

if __name__ == '__main__':
    create_db_and_tables()