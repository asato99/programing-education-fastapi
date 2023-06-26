
import unittest
import sys
sys.path.append("..")
from app.repositories.problem_repository import ProblemRepository
from app.models.problem import Problem
from app.types.problem import ProblemInfo, Constants
from resources.data.problem import ProblemData

class TestProblemRepository(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        pass

    def test_crud_front_end_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = Problem(problem_info.problemCd)

        # action
        ProblemRepository.regist(problem)
        ProblemRepository.save(problem) 
        ProblemRepository.delete(problem)

    @unittest.skip("temporary test")
    def test_get_by_problem_cd(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = Problem(problem_info.problemCd)

        # action
        ProblemRepository.regist(problem)
        problem = ProblemRepository.find_by_problem_cd(problem_info.problemCd)

        # assert
        expected = problem_info.problemCd
        actual = problem.get_problem_cd()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem_info)

    @unittest.skip("temporary test")
    def test_get_all_problems(self):
        # arrange
        problem_info1 = ProblemData.front_end_coding
        problem_info2 = ProblemData.description
        problem_info3 = ProblemData.select

        # action
        ProblemRepository.regist(problem_info1)
        ProblemRepository.regist(problem_info2)
        ProblemRepository.regist(problem_info3)
        problems = ProblemRepository.findAll()

        # after
        ProblemRepository.delete(problem_info1)
        ProblemRepository.delete(problem_info2)
        ProblemRepository.delete(problem_info3)



if __name__ == "__main__":
    unittest.main()