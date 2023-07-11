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