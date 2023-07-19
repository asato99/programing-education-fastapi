from app.db.tables import SubmissionDto, CodingSubmissionDto, DescriptionSubmissionDto, SelectSubmissionDto
from app.models.problem import CodingProblem
from sqlalchemy import and_
from sqlalchemy.sql import expression
from sqlalchemy.orm import aliased
from fastapi.encoders import jsonable_encoder

class SubmissionQuery():
	@classmethod
	def get_submissions(cls, param, session):
		submissions = session.query(
			SubmissionDto.created_at,
			SubmissionDto.comment
			).filter(SubmissionDto.problem_cd==param.problem_cd
			).filter(SubmissionDto.user_id==param.user_id).all()

		return cls.__format_rows(submissions)

	@classmethod
	def get_front_end_submissions(cls, param, session):
		html = aliased(CodingSubmissionDto)
		js = aliased(CodingSubmissionDto)
		css = aliased(CodingSubmissionDto)
		submissions = session.query(
			SubmissionDto.created_at,
			SubmissionDto.comment,
			html.code.label('html'),
			js.code.label('javascript'),
			css.code.label('css'),
			expression.literal(CodingProblem.FRONTEND).label('kubun')
			).outerjoin(html, and_(SubmissionDto.id==html.submission_id, html.language=='html')
			).outerjoin(js, and_(SubmissionDto.id==js.submission_id, js.language=='javascript')
			).outerjoin(css, and_(SubmissionDto.id==css.submission_id, css.language=='css')
			).filter(SubmissionDto.problem_cd==param.problem_cd
			).filter(SubmissionDto.user_id==param.user_id).all()

		return cls.__format_rows(submissions)

	@classmethod
	def get_back_end_submissions(cls, param, session):
		php = aliased(CodingSubmissionDto)
		python = aliased(CodingSubmissionDto)
		submissions = session.query(
			SubmissionDto.created_at,
			SubmissionDto.comment,
			php.code.label('php'),
			python.code.label('python'),
			expression.literal(CodingProblem.BACKEND).label('kubun')
			).outerjoin(php, and_(SubmissionDto.id==php.submission_id, php.language=='php')
			).outerjoin(python, and_(SubmissionDto.id==python.submission_id, python.language=='python')
			).filter(SubmissionDto.problem_cd==param.problem_cd
			).filter(SubmissionDto.user_id==param.user_id).all()

		return cls.__format_rows(submissions)

	@classmethod
	def get_description_submissions(cls, param, session):
		submissions = session.query(
			SubmissionDto.created_at,
			SubmissionDto.comment,
			DescriptionSubmissionDto.answer,
			).outerjoin(DescriptionSubmissionDto, SubmissionDto.id==DescriptionSubmissionDto.submission_id
			).filter(SubmissionDto.problem_cd==param.problem_cd
			).filter(SubmissionDto.user_id==param.user_id).all()

		return cls.__format_rows(submissions)

	@classmethod
	def get_select_submissions(cls, param, session):
		submissions = session.query(
			SubmissionDto.created_at,
			SubmissionDto.comment,
			SelectSubmissionDto.answer,
			).outerjoin(SelectSubmissionDto, SubmissionDto.id==SelectSubmissionDto.submission_id
			).filter(SubmissionDto.problem_cd==param.problem_cd
			).filter(SubmissionDto.user_id==param.user_id).all()

		return cls.__format_rows(submissions)

	def __format_rows(rows):
		dict_rows = []
		for row in rows:
			dict_row = row._asdict()
			dict_row['created_at'] = format(row.created_at, '%Y/%m/%d %H:%M')
			dict_rows.append(dict_row)

		return dict_rows
