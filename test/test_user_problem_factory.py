
import unittest
import sys
sys.path.append("..")
from app.factories.user_problem_factory import UserProblemFactory
from app.models.problem import Problem
from app.types.problem import Constants
from resources.data.problem import ProblemData

class TestUserProblemFactory(unittest.TestCase):

	def setUp(self):
		self.user_id = 0
	
	def test_create_user_problem(self):
		# arrange
		description = ProblemData.description
		problem = Problem(description.problemCd)

		# action
		user_problem = UserProblemFactory.create(self.user_id, problem)

		# assert
		expected = description.problemCd
		actual = user_problem.get_problem_cd()
		self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()