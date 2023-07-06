from app.models.problem import Problem, CodingProblem, FrontEndCoding, BackEndCoding, DescriptionProblem, SelectProblem
from app.types.problem import ProblemInfo, Constants as ProblemConstants

class ProblemFactory():
    @classmethod
    def create(cls, problem_info: ProblemInfo):
        if problem_info.format == ProblemConstants.CODING_FORMAT:
            problem = CodingProblem(problem_info.problem_cd)

            if problem_info.coding_problem.kubun == CodingProblem.FRONTEND:
                problem.set_coding_type(FrontEndCoding())
            elif problem_info.kubun == CodingProblem.BACKEND:
                problem.set_coding_type(BackEndCoding())

        elif problem_info.format == ProblemConstants.DESCRIPTION_FORMAT:
            problem = DescriptionProblem(problem_info.problem_cd)

        elif problem_info.format == ProblemConstants.SELECT_FORMAT:
            problem = SelectProblem(problem_info.problem_cd)

        else:
            problem = Problem(problem_info.problem_cd)
            # raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        return problem