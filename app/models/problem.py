class Problem():
    def __init__(self, problem_cd, problem_format, category, title, question):
        self.problem_cd = problem_cd
        self.problem_format = problem_format
        self.category = category
        self.title = title
        self.question = question

    def get_problem_info(self):
        print('get problem info')

class BackEndCodingProblem(Problem):
    def __init__(self, problem_cd, problem_format, category, title, question, lang)
        super.__init__(problem_cd, problem_format, category, title, question)
        self.lang = {'php':'', 'python':''}
    
