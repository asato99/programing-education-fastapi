import sys
sys.path.append("../../../")
from app.types.problem import ProblemInfo, CodingProblemInfo, FrontEndProblemInfo, BackEndProblemInfo, UserInput

class ProblemData():
    front_end_coding = ProblemInfo(
        problem_cd='front_end_coding_problem',
        title='test front title',
        question='test front question',
        format=1,
        coding_problem=CodingProblemInfo(kubun=1))

    back_end_coding = ProblemInfo(
        problem_cd='back_end_coding_problem',
        title='test back title',
        question='test back question',
        format=1,
        coding_problem=CodingProblemInfo(kubun=2))

    description = ProblemInfo(
        problem_cd='description_problem',
        title='test description title',
        question='test description question',
        format=2)

    select = ProblemInfo(
        problem_cd='select_problem',
        title='test select title',
        question='test select question',
        format=3)

    exception = ProblemInfo(
        problem_cd='exception_problem',
        title='test exception title',
        question='test exception question',
        format=0)

    php_input = UserInput(
        lang="php",
        code=""
    )
