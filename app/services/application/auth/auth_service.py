from fastapi import Header, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.db.setting import get_session
from app.db.tables import AuthTokenDto, UserDto

import hashlib
import random
import string
import textwrap
import datetime

class AuthService():

	@classmethod
	def login(cls, param):
		session = get_session()

		# SHA-256でハッシュ化
		password = hashlib.sha256(param.password.encode("utf-8")).hexdigest()

		user_dto = session.query(UserDto
			).filter(UserDto.admin_id==1
			).filter(UserDto.user_cd==param.problem_cd
			).filter(UserDto.password==password).first()

		if user_dto is None:
			return {
				'code': 200,
				'result': 1,
				'contents': contents,
			}

		contents['token'] = ''.join(random.choices(string.ascii_letters + string.digits, k=30)) 
		auth_dto = AuthTokenDto(
			token=contents['token'],
			auth_id=user_dto.user_id)
		session.add(auth_dto)
		session.commit()

		return {
			'code': 200,
			'result': 0,
			'contents': contents,
		}
	
	@classmethod
	def get_token_from_header(cls, authorization: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False))):
		if authorization is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})

		return cls.__get_user_id_by_token(authorization.credentials)

	def __get_user_id_by_token(token):
		get_user_id_sql = textwrap.dedent('''
			select
				user_id
			from
				user_token
			where
				token = '{0}'
		''').format(token).strip()

		with pg.connect(db.get_connect_info()) as conn:
			with conn.cursor() as cur:
				cur.execute(get_user_id_sql)
				rows = cur.fetchone()

		if rows is None:
			raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, headers={"WWW-Authenticate": "Bearer"})

		return rows[0]

