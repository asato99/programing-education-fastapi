from app.models.data.sqlalchemy_db import Base
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, String, Text, DateTime

from datetime import datetime
from typing import Optional

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