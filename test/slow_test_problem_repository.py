
import unittest
import sys
sys.path.append("..")
from app.repositories.problem_repository import ProblemRepository
from app.models.problem import Problem, CodingProblem, FrontEndCoding, BackEndCoding, DescriptionProblem, SelectProblem 
from app.types.problem import ProblemInfo, Constants, SelectProblemOption
from app.db.tables import ProblemDto, CodingProblemDto, CodingKubunDto 
from test.resources.data.problem import ProblemData
from test.resources.db import setting

class TestProblemRepositoryRegist(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(CodingProblemDto).delete()
        self.session.query(CodingKubunDto).delete()

    # @unittest.skip("temporary test")
    def test_regist(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = Problem(problem_info.problem_cd)

        # action
        problemRepository = ProblemRepository(self.session)
        problemRepository.regist(problem)


class TestProblemRepositorySave(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(CodingProblemDto).delete()
        self.session.query(CodingKubunDto).delete()
        problem_info = ProblemData.front_end_coding
        problem_dto = ProblemDto(
            problem_cd=problem_info.problem_cd,
            format=problem_info.format,
            admin_id=1,
            title=problem_info.title,
            question=problem_info.question)
        coding_problem_dto = CodingProblemDto(
            problem_cd=problem_info.problem_cd,
            language='html',
            code='')
        coding_kubun_dto = CodingKubunDto(
            problem_cd=problem_info.problem_cd,
            kubun=problem_info.coding_problem.kubun)

        self.session.add(problem_dto)
        self.session.add(coding_problem_dto)
        self.session.add(coding_kubun_dto)
        self.session.commit()

    # @unittest.skip("temporary test")
    def test_save(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = CodingProblem(problem_info.problem_cd)
        problem.set_coding_type(FrontEndCoding())
        problem.set_question('update question')

        # action
        problemRepository = ProblemRepository(self.session)
        problemRepository.save(problem)


class TestProblemRepositoryDelete(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(CodingProblemDto).delete()
        self.session.query(CodingKubunDto).delete()
        problem_info = ProblemData.front_end_coding
        problem_dto = ProblemDto(
            problem_cd=problem_info.problem_cd,
            format=problem_info.format,
            admin_id=1,
            title=problem_info.title,
            question=problem_info.question)
        coding_problem_dto = CodingProblemDto(
            problem_cd=problem_info.problem_cd,
            language='html',
            code='')
        coding_kubun_dto = CodingKubunDto(
            problem_cd=problem_info.problem_cd,
            kubun=problem_info.coding_problem.kubun)

        self.session.add(problem_dto)
        self.session.add(coding_problem_dto)
        self.session.add(coding_kubun_dto)
        self.session.commit()

    # @unittest.skip("temporary test")
    def test_delete(self):
        # arrange
        problem_info = ProblemData.front_end_coding
        problem = Problem(problem_info.problem_cd)

        # action
        problemRepository = ProblemRepository(self.session)
        problemRepository.delete(problem)


class TestProblemRepositoryFind(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(CodingProblemDto).delete()
        self.session.query(CodingKubunDto).delete()
        problem_info = ProblemData.front_end_coding
        problem_dto = ProblemDto(
            problem_cd=problem_info.problem_cd,
            format=problem_info.format,
            admin_id=1,
            title=problem_info.title,
            question=problem_info.question)
        coding_problem_dto = CodingProblemDto(
            problem_cd=problem_info.problem_cd,
            language='html',
            code='')
        coding_kubun_dto = CodingKubunDto(
            problem_cd=problem_info.problem_cd,
            kubun=problem_info.coding_problem.kubun)

        self.session.add(problem_dto)
        self.session.add(coding_problem_dto)
        self.session.add(coding_kubun_dto)
        self.session.commit()

    # @unittest.skip("temporary test")
    def test_find_by_cd(self):
        # arrange
        problem_info = ProblemData.front_end_coding

        # action
        problemRepository = ProblemRepository(self.session)
        problem = problemRepository.find_by_problem_cd(problem_info.problem_cd)

class TestProblemRepositoryFindList(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(CodingProblemDto).delete()
        self.session.query(CodingKubunDto).delete()
        problem_info = ProblemData.front_end_coding
        problem_dto = ProblemDto(
            problem_cd=problem_info.problem_cd,
            format=problem_info.format,
            admin_id=1,
            title=problem_info.title,
            question=problem_info.question)
        coding_problem_dto = CodingProblemDto(
            problem_cd=problem_info.problem_cd,
            language='html',
            code='')
        coding_kubun_dto = CodingKubunDto(
            problem_cd=problem_info.problem_cd,
            kubun=problem_info.coding_problem.kubun)

        self.session.add(problem_dto)
        self.session.add(coding_problem_dto)
        self.session.add(coding_kubun_dto)
        self.session.commit()

    # @unittest.skip("temporary test")
    def test_find_all(self):
        # action
        problemRepository = ProblemRepository(self.session)
        problems = problemRepository.find_all()

if __name__ == "__main__":
    unittest.main()