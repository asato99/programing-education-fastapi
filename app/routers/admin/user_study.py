from fastapi import APIRouter, Depends
from app.types.user_study import UserStudyInfo, UserStudyListInfo
from app.repositories.user_study_repository import UserStudyRepository
from app.repositories.study_repository import StudyRepository
from app.models.study import Study
from app.models.user_study import UserStudy
from app.db import setting

router = APIRouter(
    prefix="/admin/user_study",
    tags=["user_study"],
    responses={404: {"description": "Not found!"}}, 
)

study_repository = StudyRepository(setting.get_session())
user_study_repository = UserStudyRepository(setting.get_session())

@router.post('/regist')
def regist(param: UserStudyListInfo):
    for study_cd in param.study_cd_list:
        study = study_repository.find_by_cd(
            admin_id=1,
            study_cd=study_cd)
        user_study = UserStudy(
            user_id=param.user_id,
            study=study)
        user_study_repository.regist(user_study)

    return

@router.post('/delete')
def delete(param: UserStudyInfo):
    study = study_repository.find_by_cd(
        admin_id=1,
        study_cd=param.study_cd)
    user_study = UserStudy(
        user_id=param.user_id,
        study=study)
    user_study_repository.delete(user_study)
    return

@router.get('/list/{user_id}')
def get_user_study_list(user_id:int):
    user_studies = user_study_repository.find_all_on_user(user_id)
    return user_studies.export()

@router.get('/unregisted/{user_id}')
def get_unregisted_study_list(user_id:int):
    studies = study_repository.find_unregisted_studies_on_user(admin_id=1, user_id=user_id)
    return studies.export()
