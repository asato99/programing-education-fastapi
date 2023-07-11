import unittest
import sys
sys.path.append("..")
from app.models.problem import Problem
from app.models.messages import Messages
from app.models.user_problem import UserProblem
from app.models.submission import Submission
from resources.data.problem import ProblemData

class TestProblem(unittest.TestCase):

	def setUp(self):
		self.user_id = 0

	def test_user_problem(self):
		# arrange
		description = ProblemData.description
		problem = Problem(description.problem_cd)
		messages = Messages(self.user_id, description.problem_cd)

		# action
		user_problem = UserProblem(
			self.user_id,
			problem,
			messages,
			Submission(
				self.user_id,
				description.problem_cd,
				Submission.UNSUBMITTED))

		# assert
		expected = description.problem_cd
		actual = user_problem.get_problem_cd()
		self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

