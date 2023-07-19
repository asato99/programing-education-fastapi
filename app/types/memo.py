from pydantic import BaseModel

class MemoInfo(BaseModel):
	problem_cd:str
	memo:str