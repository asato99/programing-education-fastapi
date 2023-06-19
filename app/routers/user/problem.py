from fastapi import APIRouter, Depends
from pydantic import BaseModel 
from app.services.application.auth.auth_service import AuthService

router = APIRouter(
    prefix="/user/problem",
    tags=["problem"],
    responses={404: {"description": "Not found!"}}, 
)

@router.get("/get-problem-list")
def get_problem_list(user_id: int = Depends(AuthService.get_token_from_header)):
    print(user_id)