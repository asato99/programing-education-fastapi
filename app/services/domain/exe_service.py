from app.types.exe_service import ExecutionResult

class ExeService():

    SUCCESS = 0
    FAILURE = 1
    
    @classmethod
    def execute_php_code(cls, code):
        return ExecutionResult(
            result=cls.SUCCESS,
            output='',
            error=''
        )

    @classmethod
    def execute_python_code(cls, code):
        return ExecutionResult(
            result=cls.SUCCESS,
            output='',
            error=''
        )