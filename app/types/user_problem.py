from pydantic import BaseModel
from typing import List

class UserProblemInfo(BaseModel):
    user_id:int
    problem_cd:str

class UserProblemRegistInfo(BaseModel):
    user_id:int
    problem_cd_list:List[str]