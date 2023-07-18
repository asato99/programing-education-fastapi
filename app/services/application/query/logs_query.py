from app.db.tables import LogDto, InputLogDto, OutputLogDto, ErrorLogDto
from sqlalchemy import and_
from sqlalchemy.orm import aliased
from fastapi.encoders import jsonable_encoder

class LogsQuery():
	@classmethod
	def get_front_end_logs(cls, param, session):
		html_log = aliased(InputLogDto)
		js_log = aliased(InputLogDto)
		css_log = aliased(InputLogDto)
		logs = session.query(
			LogDto.created_at,
			html_log.code.label('html'),
			js_log.code.label('javascript'),
			css_log.code.label('css')
			).outerjoin(html_log, and_(LogDto.id==html_log.log_id, html_log.language=='html')
			).outerjoin(js_log, and_(LogDto.id==js_log.log_id, js_log.language=='javascript')
			).outerjoin(css_log, and_(LogDto.id==css_log.log_id, css_log.language=='css')
			).filter(LogDto.problem_cd==param.problem_cd
			).filter(LogDto.user_id==param.user_id).all()
		dict_logs = []
		for log in logs:
			dict_log = log._asdict()
			dict_log['created_at'] = format(log.created_at, '%Y/%m/%d %H:%M')
			dict_logs.append(dict_log)

		return dict_logs

	@classmethod
	def get_back_end_logs(cls, param, session):
		logs = session.query(
			LogDto.created_at,
			InputLogDto.language,
			InputLogDto.code,
			OutputLogDto.output,
			OutputLogDto.result,
			).outerjoin(InputLogDto, LogDto.id==InputLogDto.log_id
			).outerjoin(OutputLogDto, LogDto.id==OutputLogDto.log_id
			).filter(LogDto.problem_cd==param.problem_cd
			).filter(LogDto.user_id==param.user_id).all()
		dict_logs = []
		for log in logs:
			dict_log = log._asdict()
			dict_log['created_at'] = format(log.created_at, '%Y/%m/%d %H:%M')
			dict_logs.append(dict_log)

		return dict_logs
