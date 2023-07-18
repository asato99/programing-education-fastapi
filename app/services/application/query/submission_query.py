from app.db.tables import SubmissionDto, CodingSubmissionDto, DescriptionSubmissionDto, SelectSubmissionDto
from sqlalchemy import and_
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
		dict_submissions = []
		for submission in submissions:
			dict_submission = submission._asdict()
			dict_submission['created_at'] = format(submission.created_at, '%Y/%m/%d %H:%M')
			dict_submissions.append(dict_submission)

		return dict_submissions

	@classmethod
	def get_front_end_submissions(cls, param, session):
		html = aliased(CodingSubmissionDto)
		js = aliased(CodingSubmissionDto)
		css = aliased(CodingSubmissionDto)
		submissions = session.query(
			SubmissionDto.created_at,
			SubmissionDto.comment,
			html.code.label('html'),
			js.code.label('js'),
			css.code.label('css'),
			).outerjoin(html, and_(SubmissionDto.id==html.submission_id, html.language=='html')
			).outerjoin(js, and_(SubmissionDto.id==js.submission_id, js.language=='javascript')
			).outerjoin(css, and_(SubmissionDto.id==css.submission_id, css.language=='css')
			).filter(SubmissionDto.problem_cd==param.problem_cd
			).filter(SubmissionDto.user_id==param.user_id).all()
		dict_submissions = []
		for submission in submissions:
			dict_submission = submission._asdict()
			dict_submission['created_at'] = format(submission.created_at, '%Y/%m/%d %H:%M')
			dict_submissions.append(dict_submission)

		return dict_submissions