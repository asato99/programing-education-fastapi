from fastapi import APIRouter, Depends
from app.types.problem import ProblemInfo
from app.factories.problem_factory import ProblemFactory
from app.repositories.problem_repository import ProblemRepository
from app.services.domain.problem_service import ProblemService
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
    ProblemService.set_info(problem, param)
    problem_repository.regist(problem)
    return

@router.post('/save')
def save(param: ProblemInfo):
    problem = problem_repository.find_by_problem_cd(param.problem_cd)
    ProblemService.set_info(problem, param)
    problem_repository.save(problem)
    return

@router.post('/delete')
def delete(problem_cd:str):
    problem = problem_repository.find_by_problem_cd(problem_cd)
    problem_repository.delete(problem)
    return

@router.get('/find')
def get_problem(problem_cd:str):
    problem = problem_repository.find_by_problem_cd(problem_cd)
    return problem.export()

@router.get('/list')
def get_problem_list():
    problems = problem_repository.find_all()
    problem_headers = problems.get_problem_headers()
    return problem_headers