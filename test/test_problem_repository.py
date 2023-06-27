
import unittest
import sys
sys.path.append("..")
from app.repositories.problem_repository import ProblemRepository
from app.models.problem import Problem, CodingProblem, FrontEndCoding, BackEndCoding, DescriptionProblem, SelectProblem
from app.types.problem import ProblemInfo, Constants, SelectProblemOption
from resources.data.problem import ProblemData

class TestProblemRepository(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        pass

    # @unittest.skip("temporary test")
    def test_crud_front_end_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = Problem(problem_info.problemCd)

        # action
        ProblemRepository.regist(problem)
        ProblemRepository.save(problem) 
        ProblemRepository.delete(problem)

    # @unittest.skip("temporary test")
    def test_regist_front_end_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = CodingProblem(problem_info.problemCd)
        problem.set_coding_type(FrontEndCoding())

        # action
        ProblemRepository.regist(problem)

        # assert
        expected = problem_info.kubun
        actual = problem.get_coding_kubun()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem)

    # @unittest.skip("temporary test")
    def test_regist_back_end_problem(self):
        # arrange
        problem_info = ProblemData.back_end_coding
        problem = CodingProblem(problem_info.problemCd)
        problem.set_coding_type(BackEndCoding())

        # action
        ProblemRepository.regist(problem)

        # assert
        expected = problem_info.kubun
        actual = problem.get_coding_kubun()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem)

    # @unittest.skip("temporary test")
    def test_regist_description_problem(self):
        # arrange
        problem_info = ProblemData.description
        problem = DescriptionProblem(problem_info.problemCd)
        problem.set_model_answer('test answer')

        # action
        ProblemRepository.regist(problem)

        # assert
        expected = problem_info.format
        actual = problem.get_problem_format()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem)

    # @unittest.skip("temporary test")
    def test_regist_select_problem(self):
        # arrange
        problem_info = ProblemData.select
        problem = SelectProblem(problem_info.problemCd)
        options = [
            SelectProblemOption(no=1, text='test1'),
            SelectProblemOption(no=2, text='test2'),
            SelectProblemOption(no=3, text='test3'),
        ]
        problem.set_options(options)
        problem.set_answer(1)

        # action
        ProblemRepository.regist(problem)

        # assert
        expected = problem_info.format
        actual = problem.get_problem_format()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem)

    # @unittest.skip("temporary test")
    def test_get_front_end_problem(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = CodingProblem(problem_info.problemCd)
        front_end_coding = FrontEndCoding()
        front_end_coding.set_html('test html')
        problem.set_coding_type(front_end_coding)

        # action
        ProblemRepository.regist(problem)
        problem = ProblemRepository.find_by_problem_cd(problem_info.problemCd)

        # assert
        expected = 'test html'
        actual = problem.get_coding_type().get_html()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem)

    # @unittest.skip("temporary test")
    def test_get_back_end_problem(self):
        # arrange
        problem_info = ProblemData.back_end_coding
        problem = CodingProblem(problem_info.problemCd)
        back_end_coding = BackEndCoding()
        back_end_coding.set_php_code('test php code')
        problem.set_coding_type(back_end_coding)

        # action
        ProblemRepository.regist(problem)
        problem = ProblemRepository.find_by_problem_cd(problem_info.problemCd)

        # assert
        expected = 'test php code'
        actual = problem.get_coding_type().get_php_code()
        self.assertEqual(expected, actual)

        # after
        ProblemRepository.delete(problem)

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