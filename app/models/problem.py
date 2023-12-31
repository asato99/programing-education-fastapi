from app.types.problem import ProblemInfo, CodeInfo 
from app.services.domain.exe_service import ExeService

class Problem():
    NONE_FORMAT = 0
    CODING_FORMAT = 1
    DESCRIPTION_FORMAT = 2
    SELECT_FORMAT = 3

    def __init__(self, problem_cd):
        self.problem_cd = problem_cd
        self.title = ''
        self.question = ''
        self.created_at = None
        self.updated_at = None

    #
    # getter & setter
    #
    def get_problem_cd(self):
        return self.problem_cd

    def set_title(self, title):
        self.title = title

    def get_title(self):
        return self.title

    def set_question(self, question):
        self.question = question

    def get_question(self):
        return self.question

    def get_problem_format(self):
        return self.NONE_FORMAT

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_created_at(self):
        return self.created_at

    def set_updated_at(self, updated_at):
        self.updated_at = updated_at

    def get_updated_at(self):
        return self.updated_at

    #
    #   methods
    #
    def export(self):
        pass

    def export_header(self):
        return {
            'problem_cd': self.get_problem_cd(),
            'format':self.get_problem_format(),
            'title':self.get_title(),
            'question':self.get_question(),
            'created_at': format(self.get_created_at(), '%Y年%m月%d日')
        }



class CodingProblem(Problem):
    NULLCODING = 0
    FRONTEND = 1
    BACKEND = 2

    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.coding= NullCoding()

    def get_problem_format(self):
        return self.CODING_FORMAT

    def set_coding_type(self, coding):
        self.coding= coding

    def get_coding_type(self):
        return self.coding

    def get_coding_kubun(self):
        return self.coding.get_coding_kubun()

    def execute(self, code_info: CodeInfo):
        return self.coding.execute(code_info)

    def export(self):
        return {
            'problem_cd': self.get_problem_cd(),
            'format': self.get_problem_format(),
            'title': self.get_title(),
            'question': self.get_question(),
            'kubun': self.get_coding_kubun(),
            'codes': self.get_coding_type(),
        }
        
        
class FrontEndCoding():
    HTML = 'html'
    JAVASCRIPT = 'javascript'
    CSS = 'css'

    def __init__(self):
        self.html = ''
        self.javascript = ''
        self.css = ''

    def get_coding_kubun(self):
        return CodingProblem.FRONTEND

    def set_html(self, code):
        self.html = code

    def get_html(self):
        return self.html

    def set_javascript(self, code):
        self.javascript = code

    def get_javascript(self):
        return self.javascript 

    def set_css(self, code):
        self.css = code
    
    def get_css(self):
        return self.css

class BackEndCoding():
    PHP = 'php'
    PYTHON = 'python'

    def __init__(self):
        self.php = ''
        self.python = ''

    def get_coding_kubun(self):
        return CodingProblem.BACKEND

    def set_php_code(self, code):
        self.php = code

    def get_php_code(self):
        return self.php

    def set_python_code(self, code):
        self.python = code

    def get_python_code(self):
        return self.python

    def execute(self, code_info:CodeInfo):
        if code_info.language == self.PHP:
            result = ExeService.execute_php_code(code_info.code)
        else:
            result = ExeService.execute_python_code(code_info.code)

        return result

class NullCoding():
    def get_coding_kubun(self):
        return CodingProblem.NULLCODING

    def execute(self, coding_info):
        pass

class DescriptionProblem(Problem):
    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.model_answer = ''

    def get_problem_format(self):
        return self.DESCRIPTION_FORMAT

    def set_model_answer(self, model_answer):
        self.model_answer = model_answer

    def get_model_answer(self):
        return self.model_answer

    def export(self):
        return {
            'problem_cd': self.get_problem_cd(),
            'format': self.get_problem_format(),
            'title': self.get_title(),
            'question': self.get_question(),
            'model_answer': self.get_model_answer(),
            'created_at': format(self.get_created_at(), '%Y年%m月%d日')
        }

class SelectProblem(Problem):
    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.options = []
        self.answer = 0

    def get_problem_format(self):
        return self.SELECT_FORMAT

    def set_options(self, options):
        self.options = options

    def get_options(self):
        return self.options

    def set_answer(self, answer):
        self.answer = answer
    
    def get_answer(self):
        return self.answer

    def export(self):
        return {
            'problem_cd': self.get_problem_cd(),
            'format': self.get_problem_format(),
            'title': self.get_title(),
            'question': self.get_question(),
            'options': self.get_options(),
            'answer': self.get_answer(),
        }

class Problems():
    def __init__(self, problem_list):
        self.problem_list = problem_list

    def get_problem_headers(self):
        headers = []
        for problem in self.problem_list:
            header = {
                'problem_cd': problem.get_problem_cd(),
                'format': problem.get_problem_format(),
                'title': problem.get_title(),
                'created_at': format(problem.get_created_at(), '%Y年%m月%d日')
            }
            headers.append(header)
        return headers

