class Logs():
	def __init__(self, user_id, problem_cd):
		self.user_id = user_id
		self.problem_cd = problem_cd

	def add_log(self, log_info, repository):
		repository.add_log(self.user_id, self.problem_cd, log_info)