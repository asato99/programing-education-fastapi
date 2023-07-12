from pydantic import BaseModel
from typing import Optional

class TantoInfo(BaseModel):
    name:Optional[str]
    mail:str