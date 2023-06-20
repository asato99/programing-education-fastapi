from app.models.problem import BackEndCodingProblem, FrontEndCodingProblem
from app.models.types.problem import ProblemInfo, Constants as ProblemConstants

class ProblemFactory():
    @classmethod
    def create(cls, param: ProblemInfo):
        problem = {}
        if param.format == ProblemConstants.CODING_FORMAT:
            if param.kubun == ProblemConstants.FRONTEND:
                problem = FrontEndCodingProblem(param.problemCd, param.title, param.question)
        
        print(problem)
        return problem