from fastapi import APIRouter, Depends
from app.models.user import User
from app.factories.user_problem_factory import UserProblemFactory
from app.repositories.user_problem_repository import UserProblemRepository
from app.repositories.problem_repository import ProblemRepository
from app.models.submission import Submission
from app.types.user_problem import UserProblemInfo, UserProblemRegistInfo
from app.types.message import MessageInfo
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

@router.get("/submissions")
def get_submissions(param: UserProblemInfo = Depends()):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    submissions = user_problem.get_submissions(setting.get_session())
    return {
        'status': user_problem.get_submission_status(),
        'submissions': submissions
    }

@router.post("/approve")
def approve_submission(param: UserProblemInfo):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    user_problem.approve_submission()
    user_problem_repository.save(user_problem)
    return

@router.post("/disapprove")
def disapprove_submission(param: UserProblemInfo):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    user_problem.disapprove_submission()
    user_problem_repository.save(user_problem)
    return

@router.get("/messages")
def get_messages(param: UserProblemInfo = Depends()):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    return user_problem.get_messages(setting.get_session())

@router.post("/send")
def send_message(param: MessageInfo):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    user_problem.send_message(param.message_info)
    user_problem_repository.save(user_problem)
    return

@router.get("/logs")
def get_logs(param: UserProblemInfo = Depends()):
    user_problem = user_problem_repository.find_by_user_id_and_problem_cd(
        user_id=param.user_id,
        problem_cd=param.problem_cd)
    kubun = user_problem.export_problem()['kubun']
    logs = user_problem.get_logs(param, setting.get_session())
    return {
        'kubun':kubun,
        'logs':logs,
    }

