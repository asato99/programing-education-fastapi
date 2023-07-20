from fastapi import APIRouter, Depends
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.services.domain.user_service import UserService
from app.types.user import UserInfo, UserId
from app.db import setting

router = APIRouter(
    prefix="/admin/user",
    tags=["user"],
    responses={404: {"description": "Not found!"}}, 
)

user_repository = UserRepository(setting.get_session())

@router.post('/regist')
def regist(param: UserInfo):
    user = User(
        admin_id=1,
        user_cd=param.user_cd)
    UserService.set_info(user, param)
    user.regist_password(param.password)

    user_repository.regist(user)    
    return

@router.post('/save')
def save(param: UserInfo):
    user = user_repository.find_by_id(param.user_id)
    UserService.set_info(user, param)

    user_repository.save(user)
    return

@router.post('/delete')
def delete(param:UserId):
    user = user_repository.find_by_id(param.user_id)
    user_repository.delete(user)
    return

@router.get('/find')
def get_user_info(user_id:str):
    user = user_repository.find_by_id(user_id)
    return user

@router.get('/list')
def get_user_list():
    users = user_repository.find_all(admin_id=1)
    headers = users.export_headers()
    return headers