from app.types.problem import FrontEndProblemInfo
class ProblemService():

    @classmethod
    def set_fp_info(cls, problem, problem_info: FrontEndProblemInfo):
        problem.get_coding_type().set_html(problem_info.html)
        problem.get_coding_type().set_javascript(problem_info.javascript)
        problem.get_coding_type().set_css(problem_info.css)
