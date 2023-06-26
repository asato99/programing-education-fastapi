from app.db.setting import Base
from sqlalchemy.schema import Column, Sequence
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

class Coding(Base):
    __tablename__ = "coding"
    problem_cd = Column(String(30), primary_key=True)
    langage = Column(String(10), primary_key=True)
    code = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class CodingKubun(Base):
    __tablename__ = "coding_kubun"
    problem_cd = Column(String(30), primary_key=True)
    kubun = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class UserProblem(Base):
    __tablename__ = "user_problem"
    user_id = Column(Integer, primary_key=True)
    problem_cd = Column(String(30), primary_key=True)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class Log(Base):
    __tablename__ = "log"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    lang = Column(String(10))
    log = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class Submission(Base):
    __tablename__ = "submission"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    submission = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    message = Column(Text())
    read = Integer
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
