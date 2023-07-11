class Submission():
	UNSUBMITTED = 1
	SUBMITTED = 2
	APPROVED = 3
	NON＿APPROVED = 4

	def __init__(self, user_id, problem_cd, status):
		self.user_id = user_id
		self.problem_cd = problem_cd
		self.status = status
		self.adding = []
		self.removing = []

	def set_status(self, status):
		self.status = status

	def get_status(self):
		return self.status

	def approve(self):
		self.status = self.APPROVED

	def disapprove(self):
		self.status = self.NON_APPROVED

	def add_submission(self, submission):
		self.status = self.SUBMITTED
		self.adding.append(submission)

	def reset_adding(self):
		self.adding = []

	def get_adding(self):
		return self.adding