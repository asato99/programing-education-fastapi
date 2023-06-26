from app.db import setting
from app.db.tables import Problem as ProblemDao
from app.types.problem import ProblemInfo
from app.models.problem import Problems
from app.factories.problem_factory import ProblemFactory

class ProblemRepository():
    @classmethod
    def regist(cls, problem):
        print('regist')

        problemDao = ProblemDao(
            problem_cd=problem.get_problem_cd(),
            title=problem.get_title(),
            question=problem.get_question(),
            format=problem.get_problem_format(),
        )

        if problem.get_problem_format() == problem.CODING_FORMAT:
            pass

        session = setting.get_session()
        session.add(problemDao)
        session.commit()

    @classmethod
    def save(cls, problem):
        print('save')

        session = setting.get_session()
        problemDao = session.query(ProblemDao).filter(ProblemDao.problem_cd==problem.get_problem_cd()).first()
        problemDao.title = problem.get_title()
        problemDao.question = problem.get_question()

        session.commit()


    @classmethod
    def delete(cls, problem):
        print('delete')
        
        session = setting.get_session()
        session.query(ProblemDao).filter(ProblemDao.problem_cd==problem.get_problem_cd()).delete()
        session.commit()

    @classmethod
    def find_by_problem_cd(cls, problem_cd):
        session = setting.get_session()
        problemDao = session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_cd).first()

        problem = cls.__create_problem(problemDao)
        # problem = ProblemFactory.create(problem_info)
        # problem.set_title(problemDao.title)
        # problem.set_question(problemDao.question)

        return problem

    @classmethod
    def findAll(cls):
        session = setting.get_session()
        problemDaos = session.query(ProblemDao).all()

        problem_list = []
        for dao in problemDaos:
            problem = cls.__create_problem(dao)
            problem_list.append(problem)

        problems = Problems(problem_list)

        return problems

    def __create_problem(dao):
        problem = ProblemFactory.create(
            ProblemInfo(problemCd=dao.problem_cd, format=dao.format))
        problem.set_title(dao.title)
        problem.set_question(dao.question)
        return problem
        

