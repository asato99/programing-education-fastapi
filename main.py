from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import base
from app.routers.user import auth, problem, study
from app.routers.admin import problem as admin_problem, user, user_problem, study as admin_study, user_study

app = FastAPI()

origins = [
    "http://localhost:8080",
    "http://localhost:8081",
    "http://localhost:8082",
    "http://127.0.0.1:8080",
    "http://user.educational-tree.net",
    "http://admin.educational-tree.net",
    "https://user.educational-tree.net",
    "https://admin.educational-tree.net",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(base.router)
app.include_router(auth.router)
app.include_router(problem.router)
app.include_router(admin_problem.router)
app.include_router(user.router)
app.include_router(user_problem.router)
app.include_router(admin_study.router)
app.include_router(user_study.router)
app.include_router(study.router)

# if __name__ == "__main__":
#  	uvicorn.run(app, host="127.0.0.1", port=8000)
