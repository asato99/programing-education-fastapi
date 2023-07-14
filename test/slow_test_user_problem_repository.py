
import unittest
import os
import sys
import sqlalchemy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.repositories.user_problem_repository import UserProblemRepository
from app.models.problem import Problem, CodingProblem
from app.models.user_problem import UserProblem
from app.models.logs import Logs
from app.models.submission import Submission
from app.models.messages import Messages
from app.types.problem import CodeInfo
from app.types.submission import CodingSubmissionType
from app.db.tables import ProblemDto, DescriptionProblemDto, UserProblemDto, LogDto, SubmissionDto, MessageDto
from resources.db import setting

class TestUserProblemRepositoryRegist(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserProblemDto).delete()
        self.session.query(LogDto).delete()
        self.session.query(SubmissionDto).delete()
        self.session.query(MessageDto).delete()
        self.user_problem_repository = UserProblemRepository(self.session)

        self.user_id = 1
        self.problem_cd = 'test_problem'

    # @unittest.skip("temporary test")
    def test_regist(self):
        problem = Problem(self.problem_cd)
        user_problem = UserProblem(
            user_id=self.user_id,
            problem=problem,
            submission=Submission(
                user_id=self.user_id,
                problem_cd=problem.get_problem_cd(),
                status=Submission.UNSUBMITTED),
            messages=Messages(
                user_id=self.user_id,
                problem_cd=problem.get_problem_cd()))
        
        self.user_problem_repository.regist(user_problem)
        
class TestUserProblemRepositorySave(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserProblemDto).delete()
        self.session.query(LogDto).delete()
        self.session.query(SubmissionDto).delete()
        self.session.query(MessageDto).delete()
        self.user_problem_repository = UserProblemRepository(self.session)

        self.user_id = 1
        self.problem_cd = 'test_problem'

        user_problem_dto = UserProblemDto(
            user_id=self.user_id,
            problem_cd=self.problem_cd,
            status=1)

        self.session.add(user_problem_dto)
        self.session.commit()
        

    # @unittest.skip("temporary test")
    def test_change_status(self):
        problem = Problem(self.problem_cd)
        user_problem = UserProblem(
            user_id=self.user_id,
            problem=problem,
            submission=Submission(
                user_id=self.user_id,
                problem_cd=problem.get_problem_cd(),
                status=Submission.UNSUBMITTED),
            messages=Messages(
                user_id=self.user_id,
                problem_cd=problem.get_problem_cd()))
        user_problem.approve_submission()

        self.user_problem_repository.save(user_problem)

        user_problem_dto = self.session.query(UserProblemDto
            ).filter(UserProblemDto.user_id==self.user_id
            ).filter(UserProblemDto.problem_cd==self.problem_cd).one()

        expected = Submission.APPROVED
        actual = user_problem_dto.status
        self.assertEqual(expected, actual)

    def test_add_coding_submission(self):
        problem = CodingProblem(self.problem_cd)
        user_problem = UserProblem(
            user_id=self.user_id,
            problem=problem,
            submission=Submission(
                user_id=self.user_id,
                problem_cd=problem.get_problem_cd(),
                status=Submission.UNSUBMITTED),
            messages=Messages(
                user_id=self.user_id,
                problem_cd=problem.get_problem_cd()))
        code_list = [
            CodeInfo(
                language='html',
                code='test code'),
            CodeInfo(
                language='javascript',
                code='test code'),
            CodeInfo(
                language='css',
                code='test code')
        ]
        submission = CodingSubmissionType(
            comment='test submit',
            code_list=code_list)

        user_problem.submit(submission)

        self.user_problem_repository.save(user_problem)

        submission_dto = self.session.query(SubmissionDto
            ).filter(SubmissionDto.user_id==self.user_id
            ).filter(SubmissionDto.problem_cd==self.problem_cd).first()

        expected = submission
        actual = submission_dto.submission
        self.assertEqual(expected, actual)

class TestUserProblemRepositoryFind(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(DescriptionProblemDto).delete()
        self.session.query(UserProblemDto).delete()
        self.session.query(LogDto).delete()
        self.session.query(SubmissionDto).delete()
        self.session.query(MessageDto).delete()
        self.user_problem_repository = UserProblemRepository(self.session)

        self.user_id = 1
        self.problem_cd = 'test_problem'
        problem_dto = ProblemDto(
            problem_cd=self.problem_cd,
            format=2,
            title='test')
        description_dto = DescriptionProblemDto(
            problem_cd=self.problem_cd,
            model_answer='test')
        user_problem_dto = UserProblemDto(
            user_id=self.user_id,
            problem_cd=self.problem_cd,
            status=1)

        self.session.add(problem_dto)
        self.session.add(description_dto)
        self.session.add(user_problem_dto)
        self.session.commit()

    def test_match_problem_cd(self):
        user_problem = self.user_problem_repository.find_by_user_id_and_problem_cd(self.user_id, self.problem_cd)

        expected = self.problem_cd
        actual = user_problem.export_header()['problem_cd']
        self.assertEqual(expected, actual)
        
class TestUserProblemRepositoryFindAll(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(ProblemDto).delete()
        self.session.query(DescriptionProblemDto).delete()
        self.session.query(UserProblemDto).delete()
        self.session.query(LogDto).delete()
        self.session.query(SubmissionDto).delete()
        self.session.query(MessageDto).delete()
        self.user_problem_repository = UserProblemRepository(self.session)

        self.user_id = 1
        self.problem_cd1 = 'test_problem1'
        problem_dto1 = ProblemDto(
            problem_cd=self.problem_cd1,
            format=2,
            title='test')
        description_dto1 = DescriptionProblemDto(
            problem_cd=self.problem_cd1,
            model_answer='test')
        user_problem_dto1 = UserProblemDto(
            user_id=self.user_id,
            problem_cd=self.problem_cd1,
            status=1)

        self.problem_cd2 = 'test_problem2'
        problem_dto2 = ProblemDto(
            problem_cd=self.problem_cd2,
            format=2,
            title='test')
        description_dto2 = DescriptionProblemDto(
            problem_cd=self.problem_cd2,
            model_answer='test')
        user_problem_dto2 = UserProblemDto(
            user_id=self.user_id,
            problem_cd=self.problem_cd2,
            status=1)

        self.session.add(problem_dto1)
        self.session.add(description_dto1)
        self.session.add(user_problem_dto1)
        self.session.add(problem_dto2)
        self.session.add(description_dto2)
        self.session.add(user_problem_dto2)
        self.session.commit()
        
    def test_length(self):
        user_problems = self.user_problem_repository.find_all_on_user(self.user_id)
        headers = user_problems.export_headers()

        expected = 2
        actual = len(headers)
        self.assertEqual(expected, actual)

    def test_first_element_of_headers(self):
        user_problems = self.user_problem_repository.find_all_on_user(self.user_id)
        headers = user_problems.export_headers()

        expected = self.problem_cd1
        actual = headers[0]['problem_cd']
        self.assertEqual(expected, actual)

    def test_last_element_of_headers(self):
        user_problems = self.user_problem_repository.find_all_on_user(self.user_id)
        headers = user_problems.export_headers()

        expected = self.problem_cd2
        actual = headers[-1]['problem_cd']
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()