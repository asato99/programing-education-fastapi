import unittest
import sys
sys.path.append("..")
from app.factories.problem_factory import ProblemFactory
from app.types.problem import Constants
from resources.data.problem import ProblemData

class TestProblemFactory(unittest.TestCase):

    def test_create_coding_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding

        # action
        problem = ProblemFactory.create(problem_info)

        # assert
        expected = Constants.CODING_FORMAT
        actual = problem.get_problem_format()
        self.assertEqual(expected, actual)

    def test_create_description_problem(self):
        # arrange
        problem_info = ProblemData.description

        # action
        problem = ProblemFactory.create(problem_info)

        # assert
        expected = Constants.DESCRIPTION_FORMAT
        actual = problem.get_problem_format()
        self.assertEqual(expected, actual)

    def test_create_select_problem(self):
        # arrange
        problem_info = ProblemData.select

        # action
        problem = ProblemFactory.create(problem_info)

        # assert
        expected = Constants.SELECT_FORMAT
        actual = problem.get_problem_format()
        self.assertEqual(expected, actual)

    def test_create_exception(self):
        # arrange
        problem_info = ProblemData.exception

        # action
        problem = ProblemFactory.create(problem_info)

        # assert
        expected = Constants.NONE_FORMAT
        actual = problem.get_problem_format()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
