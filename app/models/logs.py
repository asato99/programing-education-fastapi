class Logs():
	def __init__(self, user_id, problem_cd):
		self.user_id = user_id
		self.problem_cd = problem_cd

		self.adding = []
		self.removing = []

	def add_log(self, log_info):
		self.adding.append(log_info)