class Problem():
    def __init__(self, problem_cd, title, question):
        self.problem_cd = problem_cd
        self.title = title
        self.question = question

    def get_problem_info(self):
        print('get problem info')

class FrontEndCodingProblem(Problem):
    CATEGORY = 'コーティング'
    def __init__(self, problem_cd, title, question):
        super().__init__(problem_cd, title, question)
        self.lang = {'html':'', 'css':'', 'javascript':''}

class BackEndCodingProblem(Problem):
    CATEGORY = 'コーティング'
    def __init__(self, problem_cd, title, question):
        super().__init__(problem_cd, title, question)
        self.lang = {'php':'', 'python':''}
    
class DescriptionProblem(Problem):
    CATEGORY = '記述式'
    def __init__(self, problem_cd, title, question):
        super().__init__(problem_cd, title, question)
        self.answer = ''

class SelectProblem(Problem):
    CATEGORY = '選択式'
    def __init__(self, problem_cd, title, question):
        super().__init__(problem_cd, title, question)
        self.options = []
        self.answer = ''