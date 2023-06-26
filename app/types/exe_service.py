from pydantic import BaseModel 

class ExecutionResult(BaseModel):
    result: int
    output: str
    error: str