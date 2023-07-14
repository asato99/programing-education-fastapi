from app.db.tables import UserProblemDto, SubmissionDto, MessageDto, LogDto
from app.repositories.problem_repository import ProblemRepository
from app.factories.user_problem_factory import UserProblemFactory
from app.models.problem import Problem
from app.models.user_problem import UserProblem, UserProblems
from app.models.messages import Messages

class UserProblemRepository():
	def __init__(self, session):
		self.session = session
		self.problem_repository = ProblemRepository(session)

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
				submission=submission.comment)
			self.session.add(submission_dto)
			self.session.refresh()

			if user_problem.get_problem_format() == Problem.CODING_FORMAT:
				for code in submission.code_list:
					coding_submission_dto = CodingSubmissionDto(
						submission_id=submission_dto.id,
						language=code.language,
						code=code.code)
					self.session.add(coding_submission_dto)


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
		self.session.query(UserProblemDto
			).filter(UserProblemDto.user_id==user_problem.get_user_id()
			).filter(UserProblemDto.problem_cd==user_problem.get_problem_cd()).delete()
		self.session.query(SubmissionDto
			).filter(SubmissionDto.user_id==user_problem.get_user_id()
			).filter(SubmissionDto.problem_cd==user_problem.get_problem_cd()).delete()
		self.session.query(LogDto
			).filter(LogDto.user_id==user_problem.get_user_id()
			).filter(LogDto.problem_cd==user_problem.get_problem_cd()).delete()

		self.session.commit()

	def find_by_user_id_and_problem_cd(self, user_id, problem_cd):
		user_problem_dto = self.session.query(UserProblemDto
			).filter(UserProblemDto.user_id==user_id
			).filter(UserProblemDto.problem_cd==problem_cd).one()
		problem = self.problem_repository.find_by_problem_cd(user_problem_dto.problem_cd)

		user_problem = UserProblemFactory.create(
			user_id=user_id,
			problem=problem,
			submit_status=user_problem_dto.status)
		user_problem.set_memo(user_problem_dto.memo)
		user_problem.set_created_at(user_problem_dto.created_at)

		return user_problem
		

	def find_all_on_user(self, user_id):
		user_problems = UserProblems(user_id)

		user_problem_dtos = self.session.query(UserProblemDto).filter(UserProblemDto.user_id==user_id).all()
		for user_problem_dto in user_problem_dtos:
			problem = self.problem_repository.find_by_problem_cd(user_problem_dto.problem_cd)
			user_problem = UserProblemFactory.create(
				user_id=user_problem_dto.user_id,
				problem=problem,
				submit_status=user_problem_dto.status)
			user_problem.set_memo(user_problem_dto.memo)
			user_problem.set_created_at(user_problem_dto.created_at)
			user_problems.add_user_problem(user_problem)

		return user_problems

