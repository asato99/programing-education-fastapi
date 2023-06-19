from fastapi import Header, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import db
import psycopg2 as pg

import hashlib
import random
import string
import textwrap
import datetime

class AuthService():

	@classmethod
	def login(cls, param):
		# SHA-256でハッシュ化
		password = hashlib.sha256(param.password.encode("utf-8")).hexdigest()

		auth_check_sql = textwrap.dedent('''
			select
				user_id
			from
				user_mst
			where
				user_cd = '{0}' and
				password = '{1}'
		''').format(param.userCd, password).strip()

		with pg.connect(db.get_connect_info()) as conn:
			with conn.cursor() as cur:
				cur.execute(auth_check_sql)
				rows = cur.fetchone()

		contents = {}
		if rows is None:
			print('none')
			result = 1
		else:
			result = 0
			contents['token'] = ''.join(random.choices(string.ascii_letters + string.digits, k=30)) 

			ins_date = datetime.datetime.today() + datetime.timedelta(hours=+9)
			insert_token_sql = textwrap.dedent('''
				insert into
					user_token
					(user_id, token, upd_at)
				values
					('{0}', '{1}', '{2}')
			''').format(rows[0], contents['token'], ins_date).strip()

			with pg.connect(db.get_connect_info()) as conn:
				with conn.cursor() as cur:
					cur.execute(insert_token_sql)


		return {'code': 200,
			'result': result,
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

