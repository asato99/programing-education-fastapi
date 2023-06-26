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

    description = ProblemInfo(
        problemCd='description_problem',
        title='test description title',
        question='test description question',
        format=2,
        kubun=1)

    select = ProblemInfo(
        problemCd='select_problem',
        title='test select title',
        question='test select question',
        format=3,
        kubun=1)

    exception = ProblemInfo(
        problemCd='exception_problem',
        title='test exception title',
        question='test exception question',
        format=0,
        kubun=1)

    php_input = UserInput(
        lang="php",
        code=""
    )
