from pydantic import BaseModel
from typing import List, Optional
from app.types.problem import CodeInfo

class CodingSubmission(BaseModel):
    code_list: List[CodeInfo]

class DescriptionSubmission(BaseModel):
    answer: str

class SelectSubmission(BaseModel):
    answer: int

class SubmissionInfo(BaseModel):
    problem_cd: str
    comment: str
    coding: Optional[CodingSubmission] = None
    description: Optional[DescriptionSubmission] = None
    select: Optional[SelectSubmission] = None
