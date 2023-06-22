from app.models.data import sqlalchemy_db
from app.models.data.sqlalchemy_db import Problem as ProblemDao
from app.models.types.problem import ProblemInfo
from app.factories.problem_factory import ProblemFactory

class ProblemRepository():
    @classmethod
    def regist(cls, problem_info: ProblemInfo):
        print('regist')

        problem = ProblemDao(
            problem_cd=problem_info.problemCd,
            title=problem_info.title,
            question=problem_info.question,
            format=problem_info.format,
        )

        session = sqlalchemy_db.get_session()
        session.add(problem)
        session.commit()

    @classmethod
    def save(cls, problem_info: ProblemInfo):
        print('save')

        session = sqlalchemy_db.get_session()
        problem = session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_info.problemCd).first()
        problem.title = problem_info.title
        problem.question = problem_info.question

        session.commit()


    @classmethod
    def destroy(cls, problem_info: ProblemInfo):
        print('delete')
        
        session = sqlalchemy_db.get_session()
        session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_info.problemCd).delete()
        session.commit()

    @classmethod
    def get_problem_by_problem_cd(cls, problem_cd):
        session = sqlalchemy_db.get_session()
        problemDao = session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_cd).first()

        problem_info = ProblemInfo(problemCd=problemDao.problem_cd, format=problemDao.format)
        problem = ProblemFactory.create(problem_info)
        problem.set_title(problemDao.title)
        problem.set_question(problemDao.question)

        return problem


        
        

