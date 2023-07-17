from app.db.tables import SubmissionDto, CodingSubmissionDto, DescriptionSubmissionDto, SelectSubmissionDto
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
