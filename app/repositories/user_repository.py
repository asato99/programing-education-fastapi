from app.db.tables import UserDto, TantoDto

class UserRepository():
	def __init__(self, session):
		self.session = session

	def __del__(self):
		self.session.close

	def regist(cls, user):
		user_dto = UserDto(
			admin_id=user.get_admin_id(),
			user_cd=user.get_user_cd(),
			user_name=user.get_name(),
			password=user.get_password(),
			mail=user.get_mail())
		self.session.add(user_dto)

		tantos = user.get_tantos()
		for tanto in tantos:
			tanto_dto = TantoDto(
				user_id=user.get_user_id(),
				name=tanto.get_name(),
				mail=tanto.get_mail())

		self.session.commit()

	def save(cls, user_problem):
		pass

	def destroy(cls, user_problem):
		pass

	def get_user_problem_by_user_id_and_problem_cd(cls, user_id, problem_cd):
		pass