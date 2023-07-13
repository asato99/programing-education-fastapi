
from fastapi import APIRouter
from pydantic import BaseModel 
from app.services.application.auth.auth_service import AuthService

router = APIRouter(
    prefix="/user/auth",
    tags=["auth"],
    responses={404: {"description": "Not found!"}}, 
)

class LoginInfo(BaseModel):
	unique_cd: str
	user_cd: str
	password: str

@router.post('/login')
def login(param: LoginInfo):
	return AuthService.login(param)