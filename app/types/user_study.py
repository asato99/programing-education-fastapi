from pydantic import BaseModel
from typing import List, Optional

class UserStudyInfo(BaseModel):
    user_id:int
    study_cd:str

class UserStudyListInfo(BaseModel):
    user_id:int
    study_cd_list: List[str]