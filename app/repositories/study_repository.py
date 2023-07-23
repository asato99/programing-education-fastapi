from app.models.study import Study, Studies
from app.db.tables import StudyDto, StudyContentDto

class StudyRepository():
	def __init__(self, session):
		self.session = session

	def __del__(self):
		self.session.close()

	def regist(self, study):
		study_dto = StudyDto(
			admin_id=study.get_admin_id(),
			study_cd=study.get_study_cd(),
			title=study.get_title())
		self.session.add(study_dto)
		self.session.flush()

		for index, content in enumerate(study.get_contents()):
			study_content_dto = StudyContentDto(
				study_id=study_dto.id,
				page=index+1,
				content=content)
			self.session.add(study_content_dto)

		self.session.commit()

	def save(self, study):
		study_dto = self.session.query(StudyDto
			).filter(StudyDto.admin_id==study.get_admin_id()
			).filter(StudyDto.study_cd==study.get_study_cd()).one()
		study_dto.title = study.get_title()

		self.session.query(StudyContentDto
			).filter(StudyContentDto.study_id==study_dto.id).delete()
		for index, content in enumerate(study.get_contents()):
			study_content_dto = StudyContentDto(
				study_id=study_dto.id,
				page=index+1,
				content=content)
			self.session.add(study_content_dto)

		self.session.commit()

	def delete(self, study):
		study_dto = self.session.query(StudyDto
			).filter(StudyDto.admin_id==study.get_admin_id()
			).filter(StudyDto.study_cd==study.get_study_cd()).one()
		self.session.query(StudyContentDto
			).filter(StudyContentDto.study_id==study_dto.id).delete()
		self.session.query(StudyDto
			).filter(StudyDto.admin_id==study.get_admin_id()
			).filter(StudyDto.study_cd==study.get_study_cd()).delete()
		
	def find_by_id(self, study_id):
		study_dto = self.session.query(StudyDto
			).filter(StudyDto.id==study_id).one()
		return self.__generate_study(study_dto)

	def find_all_on_admin(self, admin_id):
		study_dtos = self.session.query(StudyDto
			).filter(StudyDto.admin_id==admin_id).all()

		studies = Studies()
		for dto in study_dtos:
			studies.add_study(self.__generate_study(dto))

		return studies
		
	def __generate_study(self, dto):
		study_content_dtos = self.session.query(StudyContentDto
			).filter(StudyContentDto.study_id==dto.id).all()

		study = Study(
			admin_id=dto.admin_id,
			study_cd=dto.study_cd)
		study.set_title(dto.title)
		
		for content_dto in study_content_dtos:
			study.add_content(content_dto.content)

		return study