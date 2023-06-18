class AuthService():
	@classmethod
	def login(cls):
		print('login')
		return {'code': 200,
			'result': 0,
			'content': None,
			}
	