from app.models.types.problem import ProblemInfo, Constants
from app.repositories.problem_repository import ProblemRepository

class Problem():
    def __init__(self, problem_cd):
        self.problem_info = ProblemInfo(
            problemCd=problem_cd,
            format=self.get_problem_format(),
        )

    def set_title(self, title):
        self.problem_info.title = title

    def get_title(self):
        return self.problem_info.title

    def set_question(self, question):
        self.problem_info.question = question

    def get_question(self):
        return self.problem_info.question

    def set_problem_format(self, problem_format):
        self.problem_info.format = problem_format

    def get_problem_format(self):
        return Constants.NONE_FORMAT

    def regist(self):
        ProblemRepository.regist(self.problem_info)

    def save(self):
        ProblemRepository.save(self.problem_info)

    def destroy(self):
        ProblemRepository.destroy(self.problem_info)

class CodingProblem(Problem):
    def __init__(self, problem_cd):
        super().__init__(problem_cd)
        self.lang = {}

    def get_problem_format(self):
        return Constants.CODING_FORMAT
    
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