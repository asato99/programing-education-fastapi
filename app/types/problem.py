from pydantic import BaseModel 
from typing import Optional

class ProblemInfo(BaseModel):
	problemCd: str
	format: int
	kubun: Optional[int] = None
	title: Optional[str] = ''
	question: Optional[str] = ''
	codeList: Optional[list] = []
	inputCode: Optional[str] = ''
	options: Optional[list] = []
	answer: Optional[str] = ''

class SelectProblemOption(BaseModel):
	no: int
	text: str

class UserInput(BaseModel):
	lang: str
	code: str

class Constants():
	NONE_FORMAT = 0
	CODING_FORMAT = 1
	DESCRIPTION_FORMAT = 2
	SELECT_FORMAT = 3
	
	# 区分
	FRONTEND = 1
	BACKEND = 2
