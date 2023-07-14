from pydantic import BaseModel
from typing import List
from app.types.problem import CodeInfo

class CodingSubmissionType(BaseModel):
    comment: str
    code_list: List[CodeInfo]