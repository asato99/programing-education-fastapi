from app.models.problem import Problem, CodingProblem
from app.models.user_problem import UserProblem, CodingUserProblem
from app.models.messages import Messages
from app.models.logs import Logs, FrontEndLogs, BackEndLogs
from app.models.submission import Submission, FrontEndSubmission, BackEndSubmission, DescriptionSubmission, SelectSubmission
from app.types.problem import ProblemInfo

class UserProblemFactory():

	@classmethod
	def create(cls, user_id, problem, submit_status=Submission.UNSUBMITTED):
		if problem.get_problem_format() == Problem.CODING_FORMAT:
			if problem.get_coding_kubun() == CodingProblem.FRONTEND:
				submission = FrontEndSubmission(user_id, problem.get_problem_cd(), submit_status)
				logs = FrontEndLogs(user_id, problem.get_problem_cd())
			else:
				submission = BackEndSubmission(user_id, problem.get_problem_cd(), submit_status)
				logs = BackEndLogs(user_id, problem.get_problem_cd())

			user_problem = CodingUserProblem(
				user_id=user_id,
				problem=problem,
				messages=Messages(user_id, problem.get_problem_cd()),
				submission=submission,
				logs=logs)

		elif problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
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
