from fastapi import APIRouter, Depends
from app.types.study import StudyInfo
from app.repositories.study_repository import StudyRepository
from app.services.domain.study_service import StudyService
from app.models.study import Study
from app.db import setting

router = APIRouter(
    prefix="/admin/study",
    tags=["study"],
    responses={404: {"description": "Not found!"}}, 
)

study_repository = StudyRepository(setting.get_session())

@router.post('/create')
def create(param: StudyInfo):
    study = Study(
        admin_id=1,
        study_cd=param.study_cd)
    StudyService.set_study_info(study, param)
    study_repository.regist(study)
    return

@router.post('/save')
def save(param: StudyInfo):
    study = study_repository.find_by_cd(
        admin_id=1,
        study_cd=param.study_cd)
    StudyService.set_study_info(study, param)
    study_repository.save(study)
    return

@router.post('/delete')
def delete(param: StudyInfo):
    study = study_repository.find_by_cd(
        admin_id=1,
        study_cd=param.study_cd)
    study_repository.delete(study)
    return

@router.get('/find/{study_cd}')
def get_study(study_cd:str):
    study = study_repository.find_by_cd(
        admin_id=1,
        study_cd=study_cd)
    return study

@router.get('/list')
def get_study_list():
    studies = study_repository.find_all_on_admin(admin_id=1)
    return studies.export()