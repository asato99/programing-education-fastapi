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