import sys
sys.path.append("../../../")
from app.types.problem import ProblemInfo, UserInput

class ProblemData():
    front_end_coding = ProblemInfo(
        problemCd='front_end_coding_problem',
        title='test front title',
        question='test front question',
        format=1,
        kubun=1)

    back_end_coding = ProblemInfo(
        problemCd='back_end_coding_problem',
        title='test back title',
        question='test back question',
        format=1,
        kubun=2)

    description = ProblemInfo(
        problemCd='description_problem',
        title='test description title',
        question='test description question',
        answer='test answer',
        format=2)

    select = ProblemInfo(
        problemCd='select_problem',
        title='test select title',
        question='test select question',
        format=3)

    exception = ProblemInfo(
        problemCd='exception_problem',
        title='test exception title',
        question='test exception question',
        format=0)

    php_input = UserInput(
        lang="php",
        code=""
    )
