from app.models.problem import Problem
from app.models.user_problem import UserProblem, CodingUserProblem
from app.models.messages import Messages
from app.models.logs import Logs
from app.models.submission import Submission, CodingSubmission, DescriptionSubmission, SelectSubmission
from app.types.problem import ProblemInfo

class UserProblemFactory():

	@classmethod
	def create(cls, user_id, problem, submit_status=Submission.UNSUBMITTED):
		if problem.get_problem_format() == Problem.CODING_FORMAT:
			user_problem = CodingUserProblem(
				user_id=user_id,
				problem=problem,
				messages=Messages(user_id, problem.get_problem_cd()),
				submission=CodingSubmission(user_id, problem.get_problem_cd(), submit_status),
				logs=Logs(user_id, problem.get_problem_cd()))

		elif problem.get_problem_format() == Problem.CODING_FORMAT:
			user_problem = UserProblem(
				user_id=user_id,
				problem=problem,
				messages=Messages(user_id, problem.get_problem_cd()),
				submission=DescriptionSubmission(user_id, problem.get_problem_cd(), submit_status))
		else:
			user_problem = UserProblem(
				user_id=user_id,
				problem=problem,
				messages=Messages(user_id, problem.get_problem_cd()),
				submission=SelectSubmission(user_id, problem.get_problem_cd(), submit_status))

		return user_problem
