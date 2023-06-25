class Submission():
	UNSUBMITTED = 1
	SUBMITTED = 2
	APPROVED = 3
	NON＿APPROVED = 4

	def __init__(self, user_id, problem_cd):
		self.user_id = user_id
		self.problem_cd = problem_cd
		self.status = self.UNSUBMITTED

	def add_submission(self, submission, repository):
		repository.add_submission(self.user_id, self.problem_cd, submission)
		self.status = self.SUBMITTED
		