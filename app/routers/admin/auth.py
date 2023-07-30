
from fastapi import APIRouter
from app.services.application.auth.auth_service import AuthService
from app.types.auth import AdminLoginInfo

router = APIRouter(
    prefix="/admin/auth",
    tags=["auth"],
    responses={404: {"description": "Not found!"}}, 
)

@router.post('/login')
def login(param: AdminLoginInfo):
	return AuthService.admin_login(param)