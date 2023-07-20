import sys
sys.path.append("../../../")
from app.types.problem import ProblemInfo, CodingProblemInfo, FrontEndProblemInfo
from app.types.problem import BackEndProblemInfo, DescriptionProblemInfo, SelectProblemInfo, SelectProblemOption, CodeInfo

class ProblemData():
    front_end_coding = ProblemInfo(
        problem_cd='front_end_coding_problem',
        title='test front title',
        question='test front question',
        format=1,
        coding_problem=CodingProblemInfo(
            kubun=1, front_end_problem=FrontEndProblemInfo(
                html='test html',
                javascript='test js',
                css='test css')))

    back_end_coding = ProblemInfo(
        problem_cd='back_end_coding_problem',
        title='test back title',
        question='test back question',
        format=1,
        coding_problem=CodingProblemInfo(
            kubun=2, back_end_problem=BackEndProblemInfo(
                php='test php',
                python='test python')))

    description = ProblemInfo(
        problem_cd='description_problem',
        title='test description title',
        question='test description question',
        format=2,
        description_problem=DescriptionProblemInfo(
            model_answer='test model answer'
        ))

    select = ProblemInfo(
        problem_cd='select_problem',
        title='test select title',
        question='test select question',
        format=3,
        select_problem=SelectProblemInfo(
            options=[
                SelectProblemOption(
                    no=1,
                    text='test1'
                )
            ],
            answer=1
        ))

    exception = ProblemInfo(
        problem_cd='exception_problem',
        title='test exception title',
        question='test exception question',
        format=0)

    php_input = CodeInfo(
        language="php",
        code=""
    )
