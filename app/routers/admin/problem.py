from fastapi import APIRouter
from app.models.types.problem import ProblemInfo
from app.factories.problem_factory import ProblemFactory

router = APIRouter(
    prefix="/admin/problem",
    tags=["problem"],
    responses={404: {"description": "Not found!"}}, 
)

@router.post('/create')
def create(param: ProblemInfo):
	problem = ProblemFactory.create(param)
	return