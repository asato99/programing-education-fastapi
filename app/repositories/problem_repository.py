from app.db import setting
from app.db.tables import Problem as ProblemDao
from app.models.types.problem import ProblemInfo
from app.models.problem import Problems
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

        session = setting.get_session()
        session.add(problem)
        session.commit()

    @classmethod
    def save(cls, problem_info: ProblemInfo):
        print('save')

        session = setting.get_session()
        problem = session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_info.problemCd).first()
        problem.title = problem_info.title
        problem.question = problem_info.question

        session.commit()


    @classmethod
    def destroy(cls, problem_info: ProblemInfo):
        print('delete')
        
        session = setting.get_session()
        session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_info.problemCd).delete()
        session.commit()

    @classmethod
    def get_problem_by_problem_cd(cls, problem_cd):
        session = setting.get_session()
        problemDao = session.query(ProblemDao).filter(ProblemDao.problem_cd==problem_cd).first()

        problem = cls.__create_problem(problemDao)
        # problem = ProblemFactory.create(problem_info)
        # problem.set_title(problemDao.title)
        # problem.set_question(problemDao.question)

        return problem

    @classmethod
    def get_all_problems(cls):
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
        

