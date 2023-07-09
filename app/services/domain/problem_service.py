from app.types.problem import ProblemInfo, FrontEndProblemInfo, BackEndProblemInfo, DescriptionProblemInfo, SelectProblemInfo
from app.models.problem import Problem, CodingProblem

class ProblemService():

    @classmethod
    def set_info(cls, problem, problem_info: ProblemInfo):
        problem.set_title(problem_info.title)
        problem.set_question(problem_info.question)

        if problem.get_problem_format() == Problem.CODING_FORMAT:
            if problem.get_coding_type().get_coding_kubun() == CodingProblem.FRONTEND:
                cls.__set_fp_info(problem, problem_info.coding_problem.front_end_problem)
            elif problem.get_coding_type().get_coding_kubun() == CodingProblem.BACKEND:
                cls.__set_bp_info(problem, problem_info.coding_problem.back_end_problem)

        elif problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
            cls.__set_description_info(problem, problem_info.description_problem)

        elif problem.get_problem_format() == Problem.SELECT_FORMAT:
            cls.__set_select_info(problem, problem_info.select_problem)
        

    def __set_fp_info(problem, front_end_problem_info: FrontEndProblemInfo):
        problem.get_coding_type().set_html(front_end_problem_info.html)
        problem.get_coding_type().set_javascript(front_end_problem_info.javascript)
        problem.get_coding_type().set_css(front_end_problem_info.css)

    def __set_bp_info(problem, back_end_problem_info: BackEndProblemInfo):
        problem.get_coding_type().set_php_code(back_end_problem_info.php_code)
        problem.get_coding_type().set_python_code(back_end_problem_info.python_code)

    def __set_description_info(problem, description_info: DescriptionProblemInfo):
        problem.set_model_answer(description_info.model_answer)

    def __set_select_info(problem, select_info: SelectProblemInfo):
        problem.set_options(select_info.options)
        problem.set_answer(select_info.answer)
