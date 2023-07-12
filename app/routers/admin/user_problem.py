from fastapi import APIRouter, Depends
from app.models.user import User
from app.factories.user_problem_factory import UserProblemFactory
from app.repositories.user_problem_repository import UserProblemRepository
from app.repositories.problem_repository import ProblemRepository
from app.models.submission import Submission
from app.types.user_problem import UserProblemInfo, UserProblemRegistInfo
from app.db import setting

router = APIRouter(
    prefix="/admin/user_problem",
    tags=["user_problem"],
    responses={404: {"description": "Not found!"}}, 
)

problem_repository = ProblemRepository(setting.get_session())
user_problem_repository = UserProblemRepository(setting.get_session())

@router.post('/regist')
def regist(param: UserProblemRegistInfo):
    for problem_cd in param.problem_cd_list:
        problem = problem_repository.find_by_problem_cd(problem_cd)
        user_problem = UserProblemFactory.create(
            user_id=param.user_id,
            problem=problem,
            submit_status=Submission.UNSUBMITTED)
        user_problem_repository.regist(user_problem)
    return

@router.post('/delete')
def regist(param: UserProblemInfo):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    user_problem_repository.delete(user_problem)
    return


@router.get('/list')
def get_user_problem_list(user_id:str):
    user_problems = user_problem_repository.find_all_on_user(user_id)
    headers = user_problems.export_headers()
    return headers

