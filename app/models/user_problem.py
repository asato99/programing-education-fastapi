class UserProblem():
	def __init__(self, user_id, problem, messages):
		self.user_id = user_id
		self.problem = problem
		self.messages = messages
		self.submission = {}

	def get_problem_cd(self):
		return self.problem.get_problem_cd()

	def get_title(self):
		return self.problem.get_title()

	def get_problem_format(self):
		return self.problem.get_problem_format()

	def set_submission(self, submission):
		self.submission = submission

	def submit(self, submission, repository):
		self.submission.add_submission(submission, repository)


class CodingUserProblem(UserProblem):
	def __init__(self, user_id, problem, messages, logs):
		super().__init__(user_id, problem, messages)
		self.logs = logs

	def execute(self, user_input):
		result = self.problem.execute(user_input)
		self.logs.add_log(result)
		return result
