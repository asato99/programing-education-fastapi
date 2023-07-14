from pydantic import BaseModel
from typing import List

class Code(BaseModel):
    language: str
    code: str

class CodingSubmissionType(BaseModel):
    comment: str
    code_list: List[Code]