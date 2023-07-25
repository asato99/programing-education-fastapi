from app.models.study import Study, Studies
from app.models.user_study import UserStudy, UserStudies
from app.db.tables import StudyDto, StudyContentDto, UserStudyDto
from app.repositories.study_repository import StudyRepository

class UserStudyRepository():
	def __init__(self, session):
		self.session = session
		self.study_repository = StudyRepository(session)

	def __del__(self):
		self.session.close()

	def regist(self, user_study):
		user_study_dto = UserStudyDto(
			user_id=user_study.get_user_id(),
			admin_id=user_study.get_admin_id(),
			study_cd=user_study.get_study_cd())
		self.session.add(user_study_dto)
		self.session.commit()

	def delete(self, user_study):
		self.session.query(UserStudyDto
			).filter(UserStudyDto.user_id==user_study.get_user_id()
			).filter(UserStudyDto.admin_id==user_study.get_admin_id()
			).filter(UserStudyDto.study_cd==user_study.get_study_cd()).delete()

	def find_all_on_user(self, user_id):
		user_study_dtos = self.session.query(UserStudyDto
			).filter(UserStudyDto.user_id==user_id).all()

		user_studies = UserStudies()
		for dto in user_study_dtos:
			study = self.study_repository.find_by_cd(
				admin_id=dto.admin_id,
				study_cd=dto.study_cd)
			user_study = UserStudy(
				user_id=user_id,
				study=study)
			user_study.set_created_at(format(dto.created_at, "%Y年%m月%d日"))
			user_studies.add_user_study(user_study)

		return user_studies


		