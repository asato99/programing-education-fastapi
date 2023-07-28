from pydantic import BaseModel
from typing import List, Optional

class StudyInfo(BaseModel):
    admin_id:Optional[int] = None
    study_cd:str
    title:Optional[str] = ''
    contents: Optional[List[str]] = []