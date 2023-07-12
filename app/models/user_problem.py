class UserProblem():
	NORMAL = 1
	CODING = 2

	def __init__(self, user_id, problem, messages, submission):
		self.user_id = user_id
		self.problem = problem
		self.messages = messages
		self.submission = submission
		self.memo = ''

	def set_memo(self, memo):
		self.memo = memo

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

	def get_memo(self):
		return self.memo

	def submit(self, submission):
		self.submission.add_submission(submission)

	def approve_submission(self):
		self.submission.approve()

	def disapprove_submission(self):
		self.submission.disapprove()

	def get_messages_adding(self):
		return self.messages.get_adding()

	def export_header(self):
		return {
			'problem_cd': self.problem.get_problem_cd(),
			'title': self.problem.get_title(),
			'status': self.submission.get_status(),
			'format': self.problem.get_problem_format(),
		}


class CodingUserProblem(UserProblem):
	def __init__(self, user_id, problem, messages, submission, logs):
		super().__init__(user_id, problem, messages, submission)
		self.logs = logs
	
	def get_type(self):
		return UserProblem.CODING

	def get_logs_adding(self):
		return self.logs.get_adding()

	def execute(self, user_input):
		result = self.problem.execute(user_input)
		self.logs.add_log(result)
		return result

class UserProblems():
	def __init__(self, user_id):
		self.user_id = user_id
		self.user_problems = []

	def add_user_problem(self, user_problem):
		self.user_problems.append(user_problem)

	def reset_user_problems(self):
		self.user_problems = []

	def export_headers(self):
		headers = []
		for user_problem in self.user_problems:
			headers.append(user_problem.export_header())
		return headers
