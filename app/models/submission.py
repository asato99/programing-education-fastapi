class Submission():
	UNSUBMITTED = 1
	SUBMITTED = 2
	APPROVED = 3
	NON＿APPROVED = 4

	def __init__(self, user_id, problem_cd, status):
		self.user_id = user_id
		self.problem_cd = problem_cd
		self.status = status

	def set_status(self, status):
		self.status = status
		
	def add_submission(self, submission, repository):
		repository.add_submission(self.user_id, self.problem_cd, submission)
		self.status = self.SUBMITTED