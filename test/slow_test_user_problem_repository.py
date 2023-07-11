
import unittest
import os
import sys
import sqlalchemy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.repositories.user_problem_repository import UserProblemRepository
from app.models.problem import Problem
from app.models.user_problem import UserProblem
from app.models.logs import Logs
from app.models.submission import Submission
from app.models.messages import Messages
from app.db.tables import UserProblemDto, LogDto, SubmissionDto, MessageDto
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

    def test_add_submission(self):
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
        submission = 'submit test'
        user_problem.submit(submission)

        self.user_problem_repository.save(user_problem)

        submission_dto = self.session.query(SubmissionDto
            ).filter(SubmissionDto.user_id==self.user_id
            ).filter(SubmissionDto.problem_cd==self.problem_cd).first()

        expected = submission
        actual = submission_dto.submission
        self.assertEqual(expected, actual)
        


if __name__ == "__main__":
    unittest.main()