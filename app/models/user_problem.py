from app.types.logs import LogInfo, BackEndLogInfo
class UserProblem():
	NORMAL = 1
	CODING = 2

	def __init__(self, user_id, problem, messages, submission):
		self.user_id = user_id
		self.problem = problem
		self.messages = messages
		self.submission = submission
		self.memo = ''
		self.created_at = ''

	def set_memo(self, memo):
		self.memo = memo

	def set_created_at(self, created_at):
		self.created_at = created_at

	def get_type(self):
		return self.NORMAL

	def get_problem_format(self):
		return self.problem.get_problem_format()

	def get_user_id(self):
		return self.user_id

	def get_problem_cd(self):
		return self.problem.get_problem_cd()

	def get_memo(self):
		return self.memo

	def get_created_at(self):
		return self.created_at

	def get_submission_status(self):
		return self.submission.get_status()

	def get_submit_adding(self):
		return self.submission.get_adding()

	def get_submissions(self, session):
		return self.submission.get_submissions(session)

	def submit(self, submission):
		self.submission.add_submission(submission)

	def approve_submission(self):
		self.submission.approve()

	def disapprove_submission(self):
		self.submission.disapprove()

	def get_messages_adding(self):
		return self.messages.get_adding()

	def send_message(self, message_info):
		self.messages.add_message(message_info)

	def get_messages(self, session):
		return self.messages.get_messages(session)

	def export_problem(self):
		user_problem = self.problem.export()
		user_problem['memo'] = self.get_memo()
		return user_problem

	def export_header(self):
		return {
			'problem_cd': self.problem.get_problem_cd(),
			'title': self.problem.get_title(),
			'status': self.submission.get_status(),
			'format': self.get_problem_format(),
			'created_at': format(self.get_created_at(), '%Y年%m月%d日')
		}


class CodingUserProblem(UserProblem):
	def __init__(self, user_id, problem, messages, submission, logs):
		super().__init__(user_id, problem, messages, submission)
		self.logs = logs
	
	def get_type(self):
		return UserProblem.CODING

	def get_logs_adding(self):
		return self.logs.get_adding()

	def get_logs(self, param, session):
		return self.logs.get_logs(param, session)

	def add_log(self, log_info: LogInfo):
		self.logs.add_log(log_info)

	def execute(self, code_info):
		result = self.problem.execute(code_info)
		self.logs.add_log(BackEndLogInfo(
			problem_cd=self.problem.get_problem_cd(),
			code_info=code_info,
			exe_result=result))
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
