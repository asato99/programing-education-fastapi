from pydantic import BaseModel
from typing import Optional, List
from app.types.tanto import TantoInfo

class UserInfo(BaseModel):
    user_id:Optional[int] = None
    user_cd:str
    user_name:str
    password:Optional[str] = None
    mail:Optional[str] = ''
    tantos:Optional[List[TantoInfo]] = []

class UserId(BaseModel):
    user_id: int