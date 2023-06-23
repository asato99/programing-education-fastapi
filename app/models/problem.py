from app.models.types.problem import ProblemInfo, Constants

class Problem():
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
    #   repository
    #
    def regist(self, repository):
        repository.regist(ProblemInfo(
            problemCd=self.get_problem_cd(),
            format=self.get_format(),
            title=self.get_title(),
            question=self.get_question(),
        ))

    def save(self, repository):
        repository.save(ProblemInfo(
            problemCd=self.get_problem_cd(),
            format=self.get_format(),
            title=self.get_title(),
            question=self.get_question(),
        ))

    def destroy(self, repository):
        repository.destroy(ProblemInfo(
            problemCd=self.get_problem_cd(),
        ))

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