
import unittest
import sys
sys.path.append("..")
from app.repositories.problem_repository import ProblemRepository
from app.models.types.problem import ProblemInfo, Constants
from resources.data.problem import ProblemData

class TestProblemRepository(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        pass

    def test_crud_front_end_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding

        # action
        ProblemRepository.regist(problem_info)
        ProblemRepository.save(problem_info) 
        ProblemRepository.destroy(problem_info)

    def test_get_by_problem_cd(self):
        # arrange
        problem_info = ProblemData.front_end_coding

        # action
        ProblemRepository.regist(problem_info)
        problem = ProblemRepository.get_by_problem_cd(problem_info.problemCd)

        # assert
        expected = problem_info.title
        actual = problem.get_title()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()