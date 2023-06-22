import sys
sys.path.append("../../../")
from app.models.types.problem import ProblemInfo

class ProblemData():
    front_end_coding = ProblemInfo(
        problemCd='front_end_coding_problem',
        title='test title',
        question='test question',
        format=1,
        kubun=1)

    description = ProblemInfo(
        problemCd='description_problem',
        title='test title',
        question='test question',
        format=2,
        kubun=1)

    select = ProblemInfo(
        problemCd='select_problem',
        title='test title',
        question='test question',
        format=3,
        kubun=1)

    exception = ProblemInfo(
        problemCd='exception_problem',
        title='test title',
        question='test question',
        format=0,
        kubun=1)
