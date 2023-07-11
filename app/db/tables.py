from app.db.setting import Base
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import Integer, String, Text, DateTime

from datetime import datetime
from typing import Optional

class ProblemDto(Base):
    __tablename__ = "problem"
    problem_cd = Column(String(30), primary_key=True)
    admin_id = Column(Integer)
    format = Column(Integer)
    title = Column(String(50))
    question = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class CodingProblemDto(Base):
    __tablename__ = "coding_problem"
    problem_cd = Column(String(30), primary_key=True)
    language = Column(String(10), primary_key=True)
    code = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class CodingKubunDto(Base):
    __tablename__ = "coding_kubun"
    problem_cd = Column(String(30), primary_key=True)
    kubun = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class DescriptionProblemDto(Base):
    __tablename__ = "description_problem"
    problem_cd = Column(String(30), primary_key=True)
    model_answer = Column(Text())

class SelectProblemOptionDto(Base):
    __tablename__ = "select_problem_option"
    problem_cd = Column(String(30), primary_key=True)
    option_no = Column(Integer, primary_key=True)
    option_text = Column(Text())

class SelectProblemAnswerDto(Base):
    __tablename__ = "select_problem_answer"
    problem_cd = Column(String(30), primary_key=True)
    answer = Column(Integer)

class UserDto(Base):
    __tablename__ = "user_tbl"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    admin_id = Column(Integer)
    user_cd = Column(String(30))
    user_name = Column(String(30))
    password = Column(String(30))
    mail = Column(String(30))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class TantoDto(Base):
    __tablename__ = "tanto"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer)
    name = Column(String(30))
    mail = Column(String(30))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class UserProblemDto(Base):
    __tablename__ = "user_problem"
    user_id = Column(Integer, primary_key=True)
    problem_cd = Column(String(30), primary_key=True)
    status = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class LogDto(Base):
    __tablename__ = "log"
    id = Column(Integer, Sequence('log_id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    lang = Column(String(10))
    log = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class SubmissionDto(Base):
    __tablename__ = "submission"
    id = Column(Integer, Sequence('submission_id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    submission = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class MessageDto(Base):
    __tablename__ = "message"
    id = Column(Integer, Sequence('message_id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    message = Column(Text())
    read = Integer
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )
