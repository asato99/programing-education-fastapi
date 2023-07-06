from fastapi import APIRouter
from app.types.problem import ProblemInfo
from app.factories.problem_factory import ProblemFactory
from app.repositories.problem_repository import ProblemRepository
from app.db import setting

router = APIRouter(
    prefix="/admin/problem",
    tags=["problem"],
    responses={404: {"description": "Not found!"}}, 
)

problem_repository = ProblemRepository(setting.get_session())

@router.post('/create')
def create(param: ProblemInfo):
    problem = ProblemFactory.create(param)
    problem.set_title(param.title)
    problem.set_question(param.question)
    problem_repository.regist(problem)

    return