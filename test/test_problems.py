import unittest
import sys
sys.path.append("..")
from app.factories.problem_factory import ProblemFactory
from app.models.problem import Problems
from app.models.types.problem import ProblemInfo, Constants
from resources.data.problem import ProblemData

class TestProblemRepository(unittest.TestCase):

    def setUp(self):
        problem1 = ProblemFactory.create(ProblemData.front_end_coding)
        problem2 = ProblemFactory.create(ProblemData.description)
        problem3 = ProblemFactory.create(ProblemData.select)
        
        problem_list = []
        problem_list.append(problem1)
        problem_list.append(problem2)
        problem_list.append(problem3)

        self.problems = Problems(problem_list)


    @unittest.skip("temporary test")
    def test_get_problem_headers_match_first(self):
        # action
        problem_headers = self.problems.get_problem_headers()

        # assert
        expected = ProblemData.front_end_coding.title
        actual = problem_headers[0]['title']
        print(problem_headers)
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()
