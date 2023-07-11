
import unittest
import sys
sys.path.append("..")
from app.factories.problem_factory import ProblemFactory
from app.models.problem import Problem, CodingProblem, FrontEndCoding, BackEndCoding
from resources.data.problem import ProblemData

class TestProblem(unittest.TestCase):

    def test_set_title(self):
        # arrange
        problem = CodingProblem(problem_cd='test')

        # action
        title = 'set title ok'
        problem.set_title(title)

        # assert
        expected = title
        actual = problem.get_title()
        self.assertEqual(expected, actual)


    def test_check_format(self):
        # arrange
        problem = CodingProblem(problem_cd='test')

        # action
        expected = Problem.CODING_FORMAT
        actual = problem.get_problem_format()

        # assert
        self.assertEqual(expected, actual)


    def test_get_format(self):
        # arrange
        problem = CodingProblem(problem_cd='test')

        # action
        expected = Problem.CODING_FORMAT
        actual = problem.get_problem_format()

        # assert
        self.assertEqual(expected, actual)

    def test_execution_on_back_end_problem(self):
        # arrange
        problem = CodingProblem(problem_cd='test')
        problem.set_coding_type(BackEndCoding())
        user_input = ProblemData.php_input

        # action
        expected = 0
        actual = problem.execute(user_input).result
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()