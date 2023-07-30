from pydantic import BaseModel

class UserLoginInfo(BaseModel):
	unique_cd: str
	user_cd: str
	password: str

class AdminLoginInfo(BaseModel):
	unique_cd: str
	mentor_cd: str
	password: str