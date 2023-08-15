from app.models.mentor import Mentor, Mentors
from app.db.tables import MentorDto

class MentorRepository():
	def __init__(self, session):
		self.session = session

	def __del__(self):
		self.session.close()

	def regist(self, mentor):
		mentor_dto = MentorDto(
			admin_id=mentor.get_admin_id(),
			role=mentor.get_role(),
			mentor_cd=mentor.get_mentor_cd(),
			mentor_name=mentor.get_name(),
			password=mentor.get_password())
		self.session.add(mentor_dto)
		self.session.commit()

	def find_by_cd(self, admin_id, mentor_cd):
		mentor_dto = self.session.query(MentorDto
			).filter(MentorDto.admin_id==admin_id
			).filter(MentorDto.mentor_cd==mentor_cd).one()
		mentor = self.__generate_mentor(mentor_dto)

		return mentor

	def find_all(self, admin_id):
		mentor_dtos = self.session.query(MentorDto).filter(MentorDto.admin_id==admin_id).all()
		mentors = Mentors()
		for dto in mentor_dtos:
			mentor = self.__generate_mentor(dto)
			mentors.add_mentor(mentor)

		return mentors

	def __generate_mentor(self, dto):
		mentor = Mentor(
			admin_id=dto.admin_id,
			role=dto.role,
			mentor_cd=dto.mentor_cd)
		mentor.set_name(dto.mentor_name)
		mentor.set_mail(dto.mail)
		mentor.set_created_at(dto.created_at)

		return mentor
			

