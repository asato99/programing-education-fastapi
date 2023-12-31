from pydantic import BaseModel
from typing import Optional, List

class MentorInfo(BaseModel):
    admin_id:Optional[int] = None
    role:Optional[int] = 1
    mentor_cd:str
    mentor_name:str
    password:Optional[str] = None
    mail:Optional[str] = ''
