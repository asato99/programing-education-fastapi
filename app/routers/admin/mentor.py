from fastapi import APIRouter, Depends
from app.services.application.auth.auth_service import AuthService
from app.models.mentor import Mentor
from app.repositories.mentor_repository import MentorRepository
from app.types.mentor import MentorInfo
from app.db import setting

router = APIRouter(
    prefix="/admin/mentor",
    tags=["mentor"],
    responses={404: {"description": "Not found!"}}, 
)

mentor_repository = MentorRepository(setting.get_session())

@router.post('/regist')
def regist(param: MentorInfo, admin_id: int = Depends(AuthService.get_admin_id_from_header)):
    mentor = Mentor(
        admin_id=admin_id,
        role=2,
        mentor_cd=param.mentor_cd)
    mentor.set_name(param.mentor_name)
    mentor.regist_password(param.password)

    mentor_repository.regist(mentor)    
    return

@router.get('/list')
def get_mentor_list(admin_id: int = Depends(AuthService.get_admin_id_from_header)):
    mentors = mentor_repository.find_all(admin_id)
    headers = mentors.export_headers()
    return headers