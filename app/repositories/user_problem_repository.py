from app.db.tables import UserProblemDto, SubmissionDto, CodingSubmissionDto, DescriptionSubmissionDto, SelectSubmissionDto, MessageDto, LogDto, InputLogDto, OutputLogDto, ErrorLogDto
from app.repositories.problem_repository import ProblemRepository
from app.factories.user_problem_factory import UserProblemFactory
from app.models.problem import Problem, CodingProblem
from app.models.user_problem import UserProblem, UserProblems
from app.models.messages import Messages
from sqlalchemy import desc

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
		user_problem_dto.memo = user_problem.get_memo()
		
		for submission in user_problem.get_submit_adding():
			submission_dto = SubmissionDto(
				user_id=user_problem.get_user_id(),
				problem_cd=user_problem.get_problem_cd(),
				comment=submission.comment)
			self.session.add(submission_dto)
			self.session.flush()

			if user_problem.get_problem_format() == Problem.CODING_FORMAT:
				for code in submission.coding.code_list:
					coding_submission_dto = CodingSubmissionDto(
						submission_id=submission_dto.id,
						language=code.language,
						code=code.code)
					self.session.add(coding_submission_dto)

			elif user_problem.get_problem_format() == Problem.DESCRIPTION_FORMAT:
				description_submission_dto = DescriptionSubmissionDto(
					submission_id=submission_dto.id,
					answer=submission.description.answer)
				self.session.add(description_submission_dto)

			elif user_problem.get_problem_format() == Problem.SELECT_FORMAT:
				select_submission_dto = SelectSubmissionDto(
					submission_id=submission_dto.id,
					answer=submission.select.answer)
				self.session.add(select_submission_dto)

		for message_info in user_problem.get_messages_adding():
			message_dto = MessageDto(
				user_id=user_problem.get_user_id(),
				problem_cd=user_problem.get_problem_cd(),
				title=message_info.title,
				message=message_info.message,
				read=Messages.UNREAD)
			self.session.add(message_dto)

		if user_problem.get_type() == UserProblem.CODING:
			for log in user_problem.get_logs_adding():
				log_dto = LogDto(
					user_id=user_problem.get_user_id(),
					problem_cd=user_problem.get_problem_cd())
				self.session.add(log_dto)
				self.session.flush()

				if log.kubun == CodingProblem.FRONTEND:
					for code_info in log.code_list:
						input_log_dto = InputLogDto(
							log_id=log_dto.id,
							language=code_info.language,
							code=code_info.code)
						self.session.add(input_log_dto)

				elif log.kubun == CodingProblem.BACKEND:
					input_log_dto = InputLogDto(
						log_id=log_dto.id,
						language=log.code_info.language,
						code=log.code_info.code)
					self.session.add(input_log_dto)

					output_log_dto = OutputLogDto(
						log_id=log_dto.id,
						output=log.exe_result.output,
						result=log.exe_result.result)
					self.session.add(output_log_dto)

		self.session.commit()

	def delete(self, user_problem):
		self.session.query(UserProblemDto
			).filter(UserProblemDto.user_id==user_problem.get_user_id()
			).filter(UserProblemDto.problem_cd==user_problem.get_problem_cd()).delete()

		submission_dtos = self.session.query(SubmissionDto
			).filter(SubmissionDto.user_id==user_problem.get_user_id()
			).filter(SubmissionDto.problem_cd==user_problem.get_problem_cd()).all()
		for submission_dto in submission_dtos:
			self.session.query(CodingSubmissionDto
			).filter(CodingSubmissionDto.submission_id==submission_dto.id).delete()
			self.session.query(DescriptionSubmissionDto
			).filter(DescriptionSubmissionDto.submission_id==submission_dto.id).delete()
			self.session.query(SelectSubmissionDto
			).filter(SelectSubmissionDto.submission_id==submission_dto.id).delete()
		self.session.query(SubmissionDto
			).filter(SubmissionDto.user_id==user_problem.get_user_id()
			).filter(SubmissionDto.problem_cd==user_problem.get_problem_cd()).delete()

		log_dtos = self.session.query(LogDto
			).filter(LogDto.user_id==user_problem.get_user_id()
			).filter(LogDto.problem_cd==user_problem.get_problem_cd()).all()
		for log_dto in log_dtos:
			self.session.query(InputLogDto
			).filter(InputLogDto.log_id==log_dto.id).delete()
			self.session.query(OutputLogDto
			).filter(OutputLogDto.log_id==log_dto.id).delete()
			self.session.query(ErrorLogDto
			).filter(ErrorLogDto.log_id==log_dto.id).delete()
		self.session.query(LogDto
			).filter(LogDto.user_id==user_problem.get_user_id()
			).filter(LogDto.problem_cd==user_problem.get_problem_cd()).delete()

		self.session.query(MessageDto
			).filter(MessageDto.user_id==user_problem.get_user_id()
			).filter(MessageDto.problem_cd==user_problem.get_problem_cd()).delete()

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

		user_problem_dtos = self.session.query(UserProblemDto).filter(UserProblemDto.user_id==user_id).order_by(desc(UserProblemDto.created_at)).all()
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

