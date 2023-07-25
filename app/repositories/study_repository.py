from app.models.study import Study, Studies
from app.db.tables import StudyDto, StudyContentDto
from sqlalchemy import text

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

	def find_by_cd(self, admin_id, study_cd):
		study_dto = self.session.query(StudyDto
			).filter(StudyDto.admin_id==admin_id
			).filter(StudyDto.study_cd==study_cd).one()
		return self.__generate_study(study_dto)

	def find_all_on_admin(self, admin_id):
		study_dtos = self.session.query(StudyDto
			).filter(StudyDto.admin_id==admin_id).all()

		studies = Studies()
		for dto in study_dtos:
			studies.add_study(self.__generate_study(dto))

		return studies

	def find_unregisted_studies_on_user(self, admin_id, user_id):
		sql = text('''
			select
				study_cd,
				title
			from study
			where admin_id = {0}
			and study_cd not in (
				select study_cd from user_study
				where user_id = {1}
			)	
		'''.format(admin_id, user_id))

		studies = Studies()
		rows = self.session.execute(sql)
		for row in rows:
			study = Study(
				admin_id=admin_id,
				study_cd=row.study_cd)
			study.set_title(row.title)
			studies.add_study(study)
		return studies
		
	def __generate_study(self, dto):
		study_content_dtos = self.session.query(StudyContentDto
			).filter(StudyContentDto.study_id==dto.id).all()

		study = Study(
			admin_id=dto.admin_id,
			study_cd=dto.study_cd)
		study.set_title(dto.title)
		study.set_created_at(format(dto.created_at, "%Y年%m月%d日"))
		study.set_updated_at(format(dto.updated_at, "%Y年%m月%d日"))
		
		for content_dto in study_content_dtos:
			study.add_content(content_dto.content)

		return study