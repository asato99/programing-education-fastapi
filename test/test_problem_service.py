import unittest
import sys
sys.path.append("..")
from app.factories.problem_factory import ProblemFactory
from app.services.domain.problem_service import ProblemService
from app.types.problem import Constants
from resources.data.problem import ProblemData

class TestProblemFactory(unittest.TestCase):

    def test_set_problem_info_to_front_end_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = ProblemFactory.create(problem_info)
        
        # action
        ProblemService.set_problem_info(problem, problem_info)

        # assert
        expected = problem_info.coding_problem.front_end_problem.html
        actual = problem.get_coding_type().get_html()
        self.assertEqual(expected, actual)

    def test_set_problem_info_to_back_end_problem(self):
        # arrange
        problem_info = ProblemData.back_end_coding
        problem = ProblemFactory.create(problem_info)
        
        # action
        ProblemService.set_problem_info(problem, problem_info)

        # assert
        expected = problem_info.coding_problem.back_end_problem.python_code
        actual = problem.get_coding_type().get_python_code()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
