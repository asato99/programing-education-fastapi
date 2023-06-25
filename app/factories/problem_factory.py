from app.models.problem import Problem, CodingProblem, DescriptionProblem, SelectProblem
from app.models.types.problem import ProblemInfo, Constants as ProblemConstants

class ProblemFactory():
    @classmethod
    def create(cls, param: ProblemInfo):
        if param.format == ProblemConstants.CODING_FORMAT:
            problem = CodingProblem(param.problemCd)

        elif param.format == ProblemConstants.DESCRIPTION_FORMAT:
            problem = DescriptionProblem(param.problemCd)

        elif param.format == ProblemConstants.SELECT_FORMAT:
            problem = SelectProblem(param.problemCd)

        else:
            problem = Problem(param.problemCd)
            # raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        return problem