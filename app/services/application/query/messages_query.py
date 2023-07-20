from app.db.tables import MessageDto
from sqlalchemy import and_, desc
from sqlalchemy.sql import expression
from sqlalchemy.orm import aliased
from fastapi.encoders import jsonable_encoder

class MessagesQuery():
	@classmethod
	def get_messages(cls, param, session):
		messages = session.query(
			MessageDto.created_at,
			MessageDto.message,
			MessageDto.title,
			).filter(MessageDto.problem_cd==param.problem_cd
			).filter(MessageDto.user_id==param.user_id).order_by(desc(MessageDto.id)).all()

		return cls.__format_rows(messages)

	def __format_rows(rows):
		dict_rows = []
		for row in rows:
			dict_row = row._asdict()
			dict_row['created_at'] = format(row.created_at, '%Y/%m/%d %H:%M')
			dict_rows.append(dict_row)

		return dict_rows
