from fastapi import APIRouter, Depends
from app.services.application.auth.auth_service import AuthService
from app.types.user_study import UserStudyInfo
from app.repositories.user_study_repository import UserStudyRepository
from app.repositories.study_repository import StudyRepository
from app.models.study import Study
from app.models.user_study import UserStudy
from app.db import setting

router = APIRouter(
    prefix="/user/study",
    tags=["study"],
    responses={404: {"description": "Not found!"}}, 
)

study_repository = StudyRepository(setting.get_session())
user_study_repository = UserStudyRepository(setting.get_session())

@router.get('/find/{study_cd}')
def get_study(study_cd:str):
    study = study_repository.find_by_cd(
        admin_id=1,
        study_cd=study_cd)
    return study

@router.get('/list')
def get_user_study_list(user_id: int = Depends(AuthService.get_user_id_from_header)):
    user_studies = user_study_repository.find_all_on_user(user_id)
    return user_studies.export()
