from app.models.problem import CodingProblem, DescriptionProblem, SelectProblem
from app.models.types.problem import ProblemInfo, Constants as ProblemConstants

class ProblemFactory():
    @classmethod
    def create(cls, param: ProblemInfo):
        problem = {}
        if param.format == ProblemConstants.CODING_FORMAT:
            problem = CodingProblem(param.problemCd, param.title, param.question)

        elif param.format == ProblemConstants.DESCRIPTION_FORMAT:
            problem = DescriptionProblem(param.problemCd, param.title, param.question)

        elif param.format == ProblemConstants.SELECT_FORMAT:
            problem = SelectProblem(param.problemCd, param.title, param.question)
        
        print(problem)
        return problem