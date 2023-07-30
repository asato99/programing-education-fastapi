from fastapi import Header, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.setting import get_session
from app.db.tables import AuthTokenDto, UserDto, MentorDto, AdminManagerDto

import hashlib
import random
import string
import textwrap
from datetime import datetime, timedelta

class AuthService():

	@classmethod
	def login(cls, param):
		session = get_session()

		# SHA-256でハッシュ化
		password = hashlib.sha256(param.password.encode("utf-8")).hexdigest()

		user_dto = session.query(UserDto
			).filter(UserDto.admin_id==1
			).filter(UserDto.user_cd==param.user_cd
			).filter(UserDto.password==password).first()

		if user_dto is None:
			return {
				'code': 200,
				'result': 1,
			}

		token = ''.join(random.choices(string.ascii_letters + string.digits, k=30)) 
		auth_dto = AuthTokenDto(
			token=token,
			auth_id=user_dto.user_id)
		session.add(auth_dto)
		session.commit()

		return {
			'code': 200,
			'result': 0,
			'contents': { 'token': token },
		}
	
	@classmethod
	def get_user_id_from_header(cls, authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
		if authorization is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})

		return cls.__get_user_id_by_token(authorization.credentials)

	def __get_user_id_by_token(token):
		session = get_session()
		row = session.query(AuthTokenDto).filter(AuthTokenDto.token==token).first()

		if row is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})

		user = session.query(UserDto).filter(UserDto.user_id==row.auth_id).one()
		user.accessed_at = datetime.now() + timedelta(hours=+9)
		session.commit()

		return row.auth_id

	@classmethod
	def admin_login(cls, param):
		session = get_session()

		# SHA-256でハッシュ化
		password = hashlib.sha256(param.password.encode("utf-8")).hexdigest()
		print(password)

		mentor_dto = session.query(MentorDto
			).join(AdminManagerDto, MentorDto.admin_id == AdminManagerDto.admin_id
			).filter(AdminManagerDto.unique_cd==param.unique_cd
			).filter(MentorDto.mentor_cd==param.mentor_cd
			).filter(MentorDto.password==password).first()

		if mentor_dto is None:
			return {
				'code': 200,
				'result': 1,
			}

		token = ''.join(random.choices(string.ascii_letters + string.digits, k=30)) 
		auth_dto = AuthTokenDto(
			token=token,
			auth_id=mentor_dto.admin_id)
		session.add(auth_dto)
		session.commit()

		return {
			'code': 200,
			'result': 0,
			'contents': { 'token': token },
		}

	@classmethod
	def get_admin_id_from_header(cls, authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
		if authorization is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})

		return cls.__get_admin_id_by_token(authorization.credentials)

	def __get_admin_id_by_token(token):
		session = get_session()
		row = session.query(AuthTokenDto).filter(AuthTokenDto.token==token).first()

		if row is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})

		return row.auth_id

