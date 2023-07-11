from app.db.tables import UserProblemDto, SubmissionDto, MessageDto, LogDto
from app.models.user_problem import UserProblem
from app.models.messages import Messages

class UserProblemRepository():
	def __init__(self, session):
		self.session = session

	def __del__(self):
		self.session.close

	def regist(self, user_problem):
		user_problem_dto = UserProblemDto(
			user_id=user_problem.get_user_id(),
			problem_cd=user_problem.get_problem_cd(),
			status=user_problem.get_submission_status())
		self.session.add(user_problem_dto)
		self.session.commit()

	def save(self, user_problem):
		user_problem_dto = self.session.query(UserProblemDto).filter(
			UserProblemDto.user_id == user_problem.get_user_id()).filter(
				UserProblemDto.problem_cd == user_problem.get_problem_cd()).one()
		user_problem_dto.status = user_problem.get_submission_status()
		
		for submission in user_problem.get_submit_adding():
			submission_dto = SubmissionDto(
				user_id=user_problem.get_user_id(),
				problem_cd=user_problem.get_problem_cd(),
				submission=submission)
			self.session.add(submission_dto)

		for message in user_problem.get_messages_adding():
			message_dto = MessageDto(
				user_id=user_problem.get_user_id(),
				problem_cd=user_problem.get_problem_cd(),
				message=message,
				read=Message.UNREAD)
			self.session.add(message_dto)

		if user_problem.get_type() == UserProblem.CODING:
			for log in user_problem.get_log_adding():
				log_dto = LogDto(
					user_id=user_problem.get_user_id(),
					problem_cd=user_problem.get_problem_cd(),
					lang=log.lang,
					log=log.code)
				self.session.add(log_dto)

		self.session.commit()

	def delete(self, user_problem):
		pass

	def find_by_user_id_and_problem_cd(self, user_id, problem_cd):
		pass