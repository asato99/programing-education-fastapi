import unittest
import sys
sys.path.append("..")
from app.models.problem import Problem
from app.models.user_problem import UserProblem
from app.models.submission import Submission
from app.models.types.problem import Constants
from resources.data.problem import ProblemData

class TestProblem(unittest.TestCase):

	def setUp(self):
		self.user_id = 0

	def test_user_problem(self):
		# arrange
		description = ProblemData.description
		problem = Problem(description.problemCd)

		# action
		user_problem = UserProblem(
			self.user_id,
			problem)
		user_problem.set_submission(Submission(
			self.user_id,
			description.problemCd))

		# assert
		expected = description.format
		actual = user_problem.get_problem_format()
		self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

