
from fastapi import APIRouter
from pydantic import BaseModel 
from app.services.application.auth.auth_service import AuthService

router = APIRouter(
    prefix="/user/auth",
    tags=["auth"],
    responses={404: {"description": "Not found!"}}, 
)

class LoginInfo(BaseModel):
	uqCd: str
	userCd: str
	password: str

@router.post('/login')
def login(param: LoginInfo):
	print(param.password)
	return AuthService.login(param)