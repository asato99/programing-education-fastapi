from app.models.user import User, Users
from app.models.tanto import Tanto
from app.db.tables import UserDto, TantoDto, UserProblemDto, LogDto, InputLogDto, OutputLogDto, ErrorLogDto, SubmissionDto, CodingSubmissionDto, DescriptionSubmissionDto, SelectSubmissionDto, MessageDto

class UserRepository():
	def __init__(self, session):
		self.session = session

	def __del__(self):
		self.session.close

	def regist(self, user):
		user_dto = UserDto(
			admin_id=user.get_admin_id(),
			user_cd=user.get_cd(),
			user_name=user.get_name(),
			password=user.get_password(),
			mail=user.get_mail())
		self.session.add(user_dto)

		tantos = user.get_tantos()
		for tanto in tantos:
			tanto_dto = TantoDto(
				user_id=user.get_user_id(),
				name=tanto.get_name(),
				mail=tanto.get_mail())
			self.session.add(tanto_dto)

		self.session.commit()

	def save(self, user):
		user_dto = self.session.query(UserDto).filter(UserDto.user_id==user.get_user_id()).one()
		user_dto.user_name = user.get_name()
		user_dto.password = user.get_password()
		user_dto.mail = user.get_mail()
		
		self.session.query(TantoDto).filter(TantoDto.user_id==user.get_user_id()).delete()
		for tanto in user.get_tantos():
			tanto_dto = TantoDto(
				user_id=user.get_user_id(),
				name=tanto.get_name(),
				mail=tanto.get_mail())
			self.session.add(tanto_dto)

		self.session.commit()

	def delete(self, user):
		self.session.query(UserDto).filter(UserDto.user_id==user.get_user_id()).delete()
		self.session.query(TantoDto).filter(TantoDto.user_id==user.get_user_id()).delete()

		self.session.query(UserProblemDto
			).filter(UserProblemDto.user_id==user.get_user_id()).delete()
			
		submission_dtos = self.session.query(SubmissionDto
			).filter(SubmissionDto.user_id==user.get_user_id()).all()
		for submission_dto in submission_dtos:
			self.session.query(CodingSubmissionDto
			).filter(CodingSubmissionDto.submission_id==submission_dto.id).delete()
			self.session.query(DescriptionSubmissionDto
			).filter(DescriptionSubmissionDto.submission_id==submission_dto.id).delete()
			self.session.query(SelectSubmissionDto
			).filter(SelectSubmissionDto.submission_id==submission_dto.id).delete()
		self.session.query(SubmissionDto
			).filter(SubmissionDto.user_id==user.get_user_id()).delete()

		log_dtos = self.session.query(LogDto
			).filter(LogDto.user_id==user.get_user_id()).all()
		for log_dto in log_dtos:
			self.session.query(InputLogDto
			).filter(InputLogDto.log_id==log_dto.id).delete()
			self.session.query(OutputLogDto
			).filter(OutputLogDto.log_id==log_dto.id).delete()
			self.session.query(ErrorLogDto
			).filter(ErrorLogDto.log_id==log_dto.id).delete()
		self.session.query(LogDto
			).filter(LogDto.user_id==user.get_user_id()).delete()

		self.session.query(MessageDto
			).filter(MessageDto.user_id==user.get_user_id()).delete()

		self.session.commit()

	def find_by_id(self, user_id):
		user_dto = self.session.query(UserDto).filter(UserDto.user_id==user_id).one()
		user = User(
			admin_id=user_dto.admin_id,
			user_cd=user_dto.user_cd,
		)
		self.__set_user_info(user, user_dto)

		return user

	def find_all(self, admin_id):
		user_dtos = self.session.query(UserDto).filter(UserDto.admin_id==admin_id).all()
		users = Users(admin_id)
		for user_dto in user_dtos:
			user = User(
				admin_id=admin_id,
				user_cd=user_dto.user_cd,
			)
			self.__set_user_info(user, user_dto)
			users.add_user(user)

		return users

	def __set_user_info(self, user, dto):
		user.set_user_id(dto.user_id)
		user.set_name(dto.user_name) 
		user.set_mail(dto.mail) 
		user.set_password(dto.password) 
		user.set_created_at(dto.created_at)
		user.set_accessed_at(dto.accessed_at)

		user.reset_tantos()
		tanto_dtos = self.session.query(TantoDto).filter(TantoDto.user_id==dto.user_id).all()
		for tanto_dto in tanto_dtos:
			tanto = Tanto()
			tanto.set_name(tanto_dto.name)
			tanto.set_mail(tanto_dto.mail)
			user.add_tanto(tanto)
		