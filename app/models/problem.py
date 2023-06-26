from app.types.problem import ProblemInfo, UserInput, Constants
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
        return Constants.NONE_FORMAT

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
    def get_header(self):
        return {
            'problem_cd': self.get_problem_cd(),
            'problem_format':self.get_format(),
            'title':self.get_title(),
            'question':self.get_question(),
        }



class CodingProblem(Problem):
    FRONTEND = 1
    BACKEND = 2

    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.coding= NullCoding()

    def get_problem_format(self):
        return Constants.CODING_FORMAT

    def set_coding_type(self, coding):
        self.coding= coding

    def execute(self, user_input: UserInput):
        return self.coding.execute(user_input)
        
        
class FrontEndCoding():
    HTML = 'html'
    JAVASCRIPT = 'javascript'
    CSS = 'css'

    def __init__(self):
        self.html = ''
        self.javascript = ''
        self.css = ''

    def set_html(self, code):
        self.html = code

    def set_javascript(self, code):
        self.javascript = code

    def set_css(self, code):
        self.css = code

class BackEndCoding():
    PHP = 'php'
    PYTHON = 'python'

    def __init__(self):
        self.php_code = ''
        self.python_code = ''

    def set_php_code(self, code):
        self.php_code = code

    def set_python_code(self, code):
        self.python_code = code

    def execute(self, user_input):
        if user_input.lang == self.PHP:
            result = ExeService.execute_php_code(user_input.code)
        else:
            result = ExeService.execute_python_code(user_input.code)

        return result

class NullCoding():
    def execute(self, user_input):
        return None
    
class DescriptionProblem(Problem):
    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.answer = ''

    def get_problem_format(self):
        return Constants.DESCRIPTION_FORMAT

class SelectProblem(Problem):
    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.options = []
        self.answer = ''

    def get_problem_format(self):
        return Constants.SELECT_FORMAT

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
            }
            headers.append(header)
        return headers

