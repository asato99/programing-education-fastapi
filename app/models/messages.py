from app.services.application.query.messages_query import MessagesQuery
from app.types.user_problem import UserProblemInfo
class Messages():
	UNREAD = 0
	READ = 1

	def __init__(self, user_id, problem_cd):
		self.user_id = user_id
		self.problem_cd = problem_cd
		self.adding = []
		self.removing = []

	def add_message(self, message):
		self.adding.append(message)

	def reset_adding(self):
		self.adding = []

	def get_adding(self):
		return self.adding

	def get_messages(self, session):
		user_problem_info = UserProblemInfo(
			user_id=self.user_id,
			problem_cd=self.problem_cd)
		return MessagesQuery.get_messages(user_problem_info, session)