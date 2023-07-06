from app.types.problem import ProblemInfo
from app.db.tables import Problem, CodingProblem

class ProblemService():

    @classmethod
    def set_problem_info(cls, problem, problem_info: ProblemInfo):
        problem.set_title(param.title)
        problem.set_question(param.question)

        if problem.get_problem_format() == Problem.CODING_FORMAT:
            if problem.get_coding_type().get_coding_kubun() == CodingProblem.FRONTEND:
                self.__set_fp_info(problem, problem_info)
            elif problem.get_coding_type().get_coding_kubun() == CodingProblem.BACKEND:
                self.__set_fp_info(problem, problem_info)

    def __set_fp_info(problem, problem_info: ProblemInfo):
        problem.get_coding_type().set_html(problem_info.html)
        problem.get_coding_type().set_javascript(problem_info.javascript)
        problem.get_coding_type().set_css(problem_info.css)

    def __set_bp_info(problem, problem_info: ProblemInfo):
        problem.get_coding_type().set_php_code(problem_info.html)
        problem.get_coding_type().set_python_code(problem_info.javascript)