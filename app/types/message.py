from pydantic import BaseModel
from typing import Optional

class Message(BaseModel):
    title: str
    message: str

class MessageInfo(BaseModel):
    user_id:int
    problem_cd:str
    message_info: Message


