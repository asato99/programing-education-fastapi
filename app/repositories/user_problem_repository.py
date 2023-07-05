from app.db.tables import UserProblemDto

class UserProblemRepository():
	def __init__(self, session):
		self.session = session

	def __del__(self):
		self.session.close

	def regist(cls, user_problem):
		user_problem_dto = UserProblemDto(
			user_id=user_problem.get_user_id(),
			problem_cd=user_problem.get_problem_cd())
		self.session.add(user_problem_dto)
		self.session.commit()

	def save(cls, user_problem):
		pass

	def destroy(cls, user_problem):
		pass

	def get_user_problem_by_user_id_and_problem_cd(cls, user_id, problem_cd):
		pass