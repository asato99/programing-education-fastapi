from pydantic import BaseModel
from typing import List, Optional

class StudyInfo(BaseModel):
    admin_id:Optional[int] = None
    study_cd:str
    title:str
    contents: List[str]