from pydantic import BaseModel 

class ProblemInfo(BaseModel):
	problemCd: str
	format: int
	kubun: int
	title: str
	question: str
	codeList: list
	inputCode: str
	options: list
	answer: str

class Constants():
	CODING_FORMAT = 1
	DESCRIPTION_FORMAT = 2
	SELECTA_FORMAT = 3
	
	# 区分
	FRONTEND = 1
	BACKEND = 2
