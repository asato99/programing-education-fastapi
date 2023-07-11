class UserProblem():
	NORMAL = 1
	CODING = 2

	def __init__(self, user_id, problem, messages, submission):
		self.user_id = user_id
		self.problem = problem
		self.messages = messages
		self.submission = submission

	def get_type(self):
		return self.NORMAL

	def get_user_id(self):
		return self.user_id

	def get_problem_cd(self):
		return self.problem.get_problem_cd()

	def get_submission_status(self):
		return self.submission.get_status()

	def get_submit_adding(self):
		return self.submission.get_adding()

	def submit(self, submission):
		self.submission.add_submission(submission)

	def approve_submission(self):
		self.submission.approve()

	def disapprove_submission(self):
		self.submission.disapprove()

	def get_messages_adding(self):
		return self.messages.get_adding()


class CodingUserProblem(UserProblem):
	def __init__(self, user_id, problem, messages, logs):
		super().__init__(user_id, problem, messages)
		self.logs = logs
	
	def get_type(self):
		return UserProblem.CODING

	def get_logs_adding(self):
		return self.logs.get_adding()

	def execute(self, user_input):
		result = self.problem.execute(user_input)
		self.logs.add_log(result)
		return result
