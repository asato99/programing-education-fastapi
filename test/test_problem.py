
import unittest
import sys
sys.path.append("..")
from app.factories.problem_factory import ProblemFactory
from app.repositories.problem_repository import ProblemRepository
from app.models.problem import Problem
from app.models.types.problem import Constants
from resources.data.problem import ProblemData

class TestProblem(unittest.TestCase):

    def test_set_title(self):
        # arrange
        problem = Problem(problem_cd='test')

        # action
        title = 'set title ok'
        problem.set_title(title)

        # assert
        expected = title
        actual = problem.get_title()
        self.assertEqual(expected, actual)

    def test_set_question(self):
        # arrange
        problem = Problem(problem_cd='test')

        # action
        question = 'set question ok'
        problem.set_question(question)

        # assert
        expected = question
        actual = problem.get_question()
        self.assertEqual(expected, actual)

    def test_get_format(self):
        # arrange
        problem = Problem(problem_cd='test')

        # action
        expected = Constants.NONE_FORMAT
        actual = problem.get_problem_format()

        # assert
        self.assertEqual(expected, actual)


    #
    #   developing test
    #

    @unittest.skip("temporary test")
    def test_regist(self):
        # arrange
        problem = Problem(problem_cd='test')
        problem.set_title('set title test')
        problem.set_question('set question test')

        # action
        repository = ProblemRepository()
        problem.regist(repository)


    @unittest.skip("temporary test")
    def test_save(self):
        # arrange
        problem = Problem(problem_cd='test')
        problem.set_title('update title test')
        problem.set_question('update question test')

        # action
        repository = ProblemRepository()
        problem.save(repository)

    @unittest.skip("temporary test")
    def test_destroy(self):
        # arrange
        problem = Problem(problem_cd='test')

        # action
        repository = ProblemRepository()
        problem.destroy(repository)

if __name__ == "__main__":
    unittest.main()