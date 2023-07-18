import os
import tempfile
import subprocess

from app.types.exe_service import ExecutionResult

class ExeService():

    SUCCESS = 0
    FAILURE = 1
    
    @classmethod
    def execute_php_code(cls, code):
        tmpdir = tempfile.TemporaryDirectory()
        file_path = tmpdir.name + '/tmpfile.php'
        with open(file_path, mode='w') as fp:
            fp.write("<?php ")
            fp.write(code)
        result = subprocess.run(['php', file_path], capture_output=True, text=True)
        tmpdir.cleanup()

        return ExecutionResult(
            result=result.returncode,
            output=result.stdout.replace(file_path,''),
            error=result.stderr.replace(file_path, ''),
        )

    @classmethod
    def execute_python_code(cls, code):
        tmpdir = tempfile.TemporaryDirectory()
        file_path = tmpdir.name + '/tmpfile.py'
        with open(file_path, mode='w') as fp:
            fp.write(code)
        result = subprocess.run(['python', file_path], capture_output=True, text=True)
        tmpdir.cleanup()

        return ExecutionResult(
            result=result.returncode,
            output=result.stdout.replace(file_path,''),
            error=result.stderr.replace(file_path, ''),
        )