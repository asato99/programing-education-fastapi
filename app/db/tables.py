from app.db.setting import Base
from sqlalchemy.schema import Column, Sequence
from sqlalchemy.types import Integer, String, Text, DateTime

from datetime import datetime
from typing import Optional

class AuthTokenDto(Base):
    __tablename__ = "auth_token"
    token = Column(String(30), primary_key=True)
    auth_id = Column(Integer)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)

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
    language = Column(String(15), primary_key=True)
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
    password = Column(String(100))
    mail = Column(String(30))
    accessed_at = Column(DateTime, nullable=True)
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
    memo = Column(Text)
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class LogDto(Base):
    __tablename__ = "log"
    id = Column(Integer, Sequence('log_id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class InputLogDto(Base):
    __tablename__ = "input_log"
    log_id = Column(Integer, primary_key=True)
    language = Column(String(15), primary_key=True)
    code = Column(Text())

class OutputLogDto(Base):
    __tablename__ = "output_log"
    log_id = Column(Integer, primary_key=True)
    result = Column(Integer)
    output = Column(Text())

class ErrorLogDto(Base):
    __tablename__ = "error_log"
    log_id = Column(Integer, primary_key=True)
    error = Column(Text())

class SubmissionDto(Base):
    __tablename__ = "submission"
    id = Column(Integer, Sequence('submission_id_seq'), primary_key=True)
    user_id = Column(Integer)
    problem_cd = Column(String(30))
    comment = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class CodingSubmissionDto(Base):
    __tablename__ = "coding_submission"
    submission_id = Column(Integer, primary_key=True)
    language = Column(String(15), primary_key=True)
    code = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class DescriptionSubmissionDto(Base):
    __tablename__ = "description_submission"
    submission_id = Column(Integer, primary_key=True)
    answer = Column(Text())
    created_at = Column(DateTime, default=datetime.now(), nullable=False)
    updated_at = Column(
        DateTime, default=datetime.now(), onupdate=datetime.now(), nullable=False
    )

class SelectSubmissionDto(Base):
    __tablename__ = "select_submission"
    submission_id = Column(Integer, primary_key=True)
    answer = Column(Integer)
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
