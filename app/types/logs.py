from pydantic import BaseModel
from typing import List
from app.types.problem import CodeInfo
from app.types.exe_service import ExecutionResult

class LogInfo(BaseModel):
	pass

class FrontEndLogInfo(LogInfo):
	kubun = 1
	code_list: List[CodeInfo] = []

class BackEndLogInfo(LogInfo):
	kubun = 2
	code_info: CodeInfo
	exe_result: ExecutionResult