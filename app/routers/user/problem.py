from fastapi import APIRouter, Depends
from pydantic import BaseModel 
from app.db.setting import get_session
from app.services.application.auth.auth_service import AuthService
from app.repositories.user_problem_repository import UserProblemRepository
from app.types.problem import ExecutionInfo, CodeInfo
from app.types.submission import SubmissionInfo
from app.types.memo import MemoInfo
from app.types.logs import FrontEndLogInfo
from app.db import setting

router = APIRouter(
    prefix="/user/problem",
    tags=["problem"],
    responses={404: {"description": "Not found!"}}, 
)

user_problem_repository = UserProblemRepository(get_session())

@router.get("/find/{problem_cd}")
def get_problem_info(problem_cd: str, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(user_id, problem_cd)
    return user_problem.export_problem()

@router.get("/codes/{problem_cd}")
def get_problem_info(problem_cd: str, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(user_id, problem_cd)
    return user_problem.export_problem()['codes']

@router.get("/list")
def get_problem_list(user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problems = user_problem_repository.find_all_on_user(user_id)
    return user_problems.export_headers()

@router.post("/execute")
def execute(param:ExecutionInfo, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(user_id, param.problem_cd)
    result = user_problem.execute(CodeInfo(
        language=param.language,
        code=param.code))
    user_problem_repository.save(user_problem)
    return result

@router.get("/submissions/{problem_cd}")
def get_submissions(problem_cd:str, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=user_id,
        problem_cd=problem_cd)
    return user_problem.get_submissions(setting.get_session())

@router.post("/submit")
def submit(param:SubmissionInfo, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(user_id, param.problem_cd)
    user_problem.submit(param)
    user_problem_repository.save(user_problem)
    return

@router.get("/messages/{problem_cd}")
def get_messages(problem_cd:str, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=user_id,
        problem_cd=problem_cd)
    return user_problem.get_messages(setting.get_session())

@router.post("/add_log")
def add_log(param:FrontEndLogInfo, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(user_id, param.problem_cd)
    user_problem.add_log(param)
    user_problem_repository.save(user_problem)
    return

@router.post("/save_memo")
def save_memo(param:MemoInfo, user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(user_id, param.problem_cd)
    user_problem.set_memo(param.memo)
    user_problem_repository.save(user_problem)
    return