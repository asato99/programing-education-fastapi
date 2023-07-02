from app.db import setting
from app.db.tables import ProblemDto, CodingProblemDto, CodingKubunDto, DescriptionProblemDto, SelectProblemOptionDto, SelectProblemAnswerDto
from app.types.problem import ProblemInfo, SelectProblemOption
from app.models.problem import Problem, CodingProblem, FrontEndCoding, BackEndCoding, Problems
from app.factories.problem_factory import ProblemFactory

class ProblemRepository():

    def __init__(self, session):
        self.session = session

    def __del__(self):
        self.session.close

    def regist(self, problem):
        problem_dto = ProblemDto(
            problem_cd=problem.get_problem_cd(),
            title=problem.get_title(),
            question=problem.get_question(),
            format=problem.get_problem_format(),
        )
        self.session.add(problem_dto)

        if problem.get_problem_format() == Problem.CODING_FORMAT:
            coding_kubun_dto = CodingKubunDto(
                problem_cd=problem.get_problem_cd(),
                kubun=problem.get_coding_kubun(),
            )
            self.session.add(coding_kubun_dto)

            if problem.get_coding_kubun() == CodingProblem.FRONTEND:
                htlm_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=FrontEndCoding.HTML,
                    code=problem.get_coding_type().get_html()
                )
                js_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=FrontEndCoding.JAVASCRIPT,
                    code=problem.get_coding_type().get_javascript()
                )
                css_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=FrontEndCoding.CSS,
                    code=problem.get_coding_type().get_css()
                )

                self.session.add(htlm_dto)
                self.session.add(js_dto)
                self.session.add(css_dto)

            elif problem.get_coding_kubun() == CodingProblem.BACKEND:
                php_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=BackEndCoding.PHP,
                    code=problem.get_coding_type().get_php_code()
                )
                python_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=BackEndCoding.PYTHON,
                    code=problem.get_coding_type().get_python_code()
                )

                self.session.add(php_dto)
                self.session.add(python_dto)

        elif problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
            description_dto = DescriptionProblemDto(
                problem_cd=problem.get_problem_cd(),
                model_answer=problem.get_model_answer()
            )
            self.session.add(description_dto)

        elif problem.get_problem_format() == Problem.SELECT_FORMAT:
            for option in problem.get_options():
                select_option_dto = SelectProblemOptionDto(
                    problem_cd=problem.get_problem_cd(),
                    option_no=option.no,
                    option_text=option.text
                )
                self.session.add(select_option_dto)

            select_answer_dto = SelectProblemAnswerDto(
                problem_cd=problem.get_problem_cd(),
                answer=problem.get_answer()
            )
            self.session.add(select_answer_dto)
            

        self.session.commit()

    def save(self, problem):
        problem_dto = self.session.query(ProblemDto).filter(ProblemDto.problem_cd==problem.get_problem_cd()).first()
        problem_dto.title = problem.get_title()
        problem_dto.question = problem.get_question()

        if problem.get_problem_format() == Problem.CODING_FORMAT:
            self.session.query(CodingProblemDto).filter(CodingProblemDto.problem_cd==problem.get_problem_cd()).delete()

            if problem.get_coding_kubun() == CodingProblem.FRONTEND:
                htlm_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=FrontEndCoding.HTML,
                    code=problem.get_coding_type().get_html()
                )
                js_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=FrontEndCoding.JAVASCRIPT,
                    code=problem.get_coding_type().get_javascript()
                )
                css_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=FrontEndCoding.CSS,
                    code=problem.get_coding_type().get_css()
                )

                self.session.add(htlm_dto)
                self.session.add(js_dto)
                self.session.add(css_dto)

            elif problem.get_coding_kubun() == CodingProblem.BACKEND:
                php_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=BackEndCoding.PHP,
                    code=problem.get_coding_type().get_php_code()
                )
                python_dto = CodingProblemDto(
                    problem_cd=problem.get_problem_cd(),
                    language=BackEndCoding.PYTHON,
                    code=problem.get_coding_type().get_python_code()
                )

                self.session.add(php_dto)
                self.session.add(python_dto)

        elif problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
            description_dto = self.session.query(DescriptionProblemDto).filter(DescriptionProblemDto.problem_cd==problem.get_problem_cd()).first()
            description_dto.set_model_answer = problem.get_model_answer()

        elif problem.get_problem_format() == Problem.SELECT_FORMAT:
            self.session.query(SelectProblemOptionDto).filter(SelectProblemOptionDto.problem_cd==problem.get_problem_cd()).delete()
            for option in problem.get_options():
                select_option_dto = SelectProblemOptionDto(
                    problem_cd=problem.get_problem_cd(),
                    option_no=option.no,
                    option_text=option.text
                )
                self.session.add(select_option_dto)

            select_answer_dto = self.session.query(SelectProblemAnswerDto).filter(SelectProblemAnswerDto.problem_cd==problem.get_problem_cd()).first()
            select_answer_dto.answer = select_answer_dto.get_answer()

        self.session.commit()


    def delete(self, problem):
        self.session.query(ProblemDto).filter(ProblemDto.problem_cd==problem.get_problem_cd()).delete()

        if problem.get_problem_format() == Problem.CODING_FORMAT:
            self.session.query(CodingKubunDto).filter(CodingKubunDto.problem_cd==problem.get_problem_cd()).delete()
            self.session.query(CodingProblemDto).filter(CodingProblemDto.problem_cd==problem.get_problem_cd()).delete()

        elif problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
            self.session.query(DescriptionProblemDto).filter(DescriptionProblemDto.problem_cd==problem.get_problem_cd()).delete()

        elif problem.get_problem_format() == Problem.SELECT_FORMAT:
            self.session.query(SelectProblemOptionDto).filter(SelectProblemOptionDto.problem_cd==problem.get_problem_cd()).delete()
            self.session.query(SelectProblemAnswerDto).filter(SelectProblemAnswerDto.problem_cd==problem.get_problem_cd()).delete()


        self.session.commit()

    def find_by_problem_cd(self, problem_cd):
        problem_dto = self.session.query(ProblemDto).filter(ProblemDto.problem_cd==problem_cd).first()

        problem = self.__create_problem(problem_dto)
        problem.set_title(problem_dto.title)
        problem.set_question(problem_dto.question)

        if problem.get_problem_format() == Problem.CODING_FORMAT:
            kubun_dto = self.session.query(CodingKubunDto).filter(CodingKubunDto.problem_cd==problem.get_problem_cd()).first()
            coding_dtos = self.session.query(CodingProblemDto).filter(CodingProblemDto.problem_cd==problem.get_problem_cd()).all()
            if kubun_dto.kubun == CodingProblem.FRONTEND:
                front_end_coding = FrontEndCoding()

                html_coding = next(filter(lambda x: x.language==FrontEndCoding.HTML, coding_dtos), None)
                front_end_coding.set_html(html_coding.code if html_coding is not None else '')

                js_coding = next(filter(lambda x: x.language==FrontEndCoding.JAVASCRIPT, coding_dtos), None)
                front_end_coding.set_javascript(js_coding.code if js_coding is not None else '')

                css_coding = next(filter(lambda x: x.language==FrontEndCoding.CSS, coding_dtos), None)
                front_end_coding.set_css(css_coding.code if css_coding is not None else '')

                problem.set_coding_type(front_end_coding)

            elif kubun_dto.kubun == CodingProblem.BACKEND:
                back_end_coding = BackEndCoding()

                php_coding = next(filter(lambda x: x.language==BackEndCoding.PHP, coding_dtos), None)
                back_end_coding.set_php_code(php_coding.code if php_coding is not None else '')

                python_coding = next(filter(lambda x: x.language==BackEndCoding.PYTHON, coding_dtos), None)
                back_end_coding.set_python_code(python_coding.code if python_coding is not None else '')

                problem.set_coding_type(back_end_coding)


        elif problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
            description_dto = self.session.query(DescriptionProblemDto).filter(DescriptionProblemDto.problem_cd==problem.get_problem_cd()).first()
            problem.set_model_answer(description_dto.model_answer)


        elif problem.get_problem_format() == Problem.SELECT_FORMAT:
            select_option_dtos = self.session.query(SelectProblemOptionDto).filter(SelectProblemOptionDto.problem_cd==problem.get_problem_cd()).all()
            select_answer_dto = self.session.query(SelectProblemAnswerDto).filter(SelectProblemAnswerDto.problem_cd==problem.get_problem_cd()).first()
            options = [SelectProblemOption(no=dto.option_no, text=dto.option_text) for dto in select_option_dtos]
            problem.set_options(options)
            problem.set_answer(select_answer_dto.answer)


        return problem

    def findAll(self):
        problem_dtos = self.session.query(ProblemDto).all()

        problem_list = []
        for dto in problem_dtos:
            problem = self.__create_problem(dto)
            problem_list.append(problem)

        problems = Problems(problem_list)

        return problems

    def __create_problem(self, dto):
        problem = ProblemFactory.create(
            ProblemInfo(problemCd=dto.problem_cd, format=dto.format))
        problem.set_title(dto.title)
        problem.set_question(dto.question)
        return problem

        
        

