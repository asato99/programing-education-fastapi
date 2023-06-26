from app.models.user_problem import UserProblem, CodingUserProblem
from app.models.messages import Messages
from app.models.logs import Logs
from app.models.submission import Submission
from app.types.problem import ProblemInfo, Constants as ProblemConstants

class UserProblemFactory():

	@classmethod
	def create(cls, user_id, problem, submission=None):
		if problem.get_problem_format() == ProblemConstants.CODING_FORMAT:
			user_problem = CodingUserProblem(
				user_id,
				problem,
				Messages(user_id, problem.get_problem_cd()),
				Logs(user_id, problem.get_problem_cd()))
		else:
			user_problem = UserProblem(
				user_id,
				problem,
				Messages(user_id, problem.get_problem_cd()))

		if submission is None:
			user_problem.set_submission(Submission(user_id, problem.get_problem_cd()))
		else:
			user_problem.set_submission(submission)

		return user_problem
