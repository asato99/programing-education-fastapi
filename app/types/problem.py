from pydantic import BaseModel 
from typing import Optional, List

class FrontEndProblemInfo(BaseModel):
	html: str
	javascript: str
	css: str

class BackEndProblemInfo(BaseModel):
	php_code: str
	python_code: str

class CodingProblemInfo(BaseModel):
	kubun: int
	front_end_problem: Optional[FrontEndProblemInfo] = None
	back_end_problem: Optional[BackEndProblemInfo] = None

class DescriptionProblemInfo(BaseModel):
	model_answer: str

class SelectProblemOption(BaseModel):
	no: int
	text: str

class SelectProblemInfo(BaseModel):
	options: List[SelectProblemOption]
	answer: int

class ProblemInfo(BaseModel):
	problem_cd: str
	format: int
	title: Optional[str] = ''
	question: Optional[str] = ''
	coding_problem: Optional[CodingProblemInfo] = None
	description_problem: Optional[DescriptionProblemInfo] = None
	select_problem: Optional[SelectProblemInfo] = None

class SubmitInfo(BaseModel):
	problem_cd: str
	comment: str
	front_end_problem_info: Optional[FrontEndProblemInfo] = None
	back_end_problem_info: Optional[BackEndProblemInfo] = None
	description_problem_info: Optional[DescriptionProblemInfo] = None
	select_problem_info: Optional[SelectProblemInfo] = None

class CodeInfo(BaseModel):
	language: str
	code: str

class ExecutionInfo(BaseModel):
	problem_cd:str
	language:str
	code:str