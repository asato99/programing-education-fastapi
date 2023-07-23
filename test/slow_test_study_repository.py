import unittest
import os
import sys
import sqlalchemy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.repositories.study_repository import StudyRepository
from app.models.study import Study, Studies
from app.db.tables import StudyDto, StudyContentDto
from resources.db import setting

class TestStudyRepositoryRegist(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(StudyDto).delete()
        self.session.query(StudyContentDto).delete()
        self.study_repository = StudyRepository(self.session)

        self.admin_id = 1
        self.study_cd = 'test_study'

    # @unittest.skip("temporary test")
    def test_regist(self):
        # arrange
        study = Study(
            admin_id=self.admin_id,
            study_cd=self.study_cd
        )
        title = 'test'
        study.set_title(title)

        self.study_repository.regist(study)

        study_dto = self.session.query(StudyDto).filter(StudyDto.study_cd==self.study_cd).first()
        expected = title
        actual = study_dto.title
        self.assertEqual(expected, actual)

class TestStudyRepositorySave(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(StudyDto).delete()
        self.session.query(StudyContentDto).delete()
        self.study_repository = StudyRepository(self.session)

        self.admin_id = 1
        self.study_cd = 'test_study'

        study_dto = StudyDto(
            admin_id=self.admin_id,
            study_cd =self.study_cd,
            title='test')
        self.session.add(study_dto)
        self.session.flush()

        study_content_dto = StudyContentDto(
            study_id=study_dto.id,
            page=1,
            content='test content')
        self.session.add(study_content_dto)
        self.session.commit()

    def test_update_title(self):
        update_title = 'update title'

        study = Study(
            admin_id=self.admin_id,
            study_cd=self.study_cd)
        study.set_title(update_title)

        self.study_repository.save(study)

        study_dto = self.session.query(StudyDto).filter(StudyDto.study_cd==self.study_cd).one()
        expected = update_title
        actual = study_dto.title
        self.assertEqual(expected, actual)

    def test_update_content(self):
        content = 'test content'
        study = Study(
            admin_id=self.admin_id,
            study_cd=self.study_cd)
        study.add_content(content)

        self.study_repository.save(study)

        study_dto = self.session.query(StudyDto).filter(StudyDto.study_cd==self.study_cd).one()
        study_content_dto = self.session.query(StudyContentDto).filter(StudyContentDto.study_id==study_dto.id).first()
        expected = content
        actual = study_content_dto.content
        self.assertEqual(expected, actual)

class TestStudyRepositoryDelete(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(StudyDto).delete()
        self.session.query(StudyContentDto).delete()
        self.study_repository = StudyRepository(self.session)

        self.admin_id = 1
        self.study_cd = 'test_study'

        study_dto = StudyDto(
            admin_id=self.admin_id,
            study_cd =self.study_cd,
            title='test')
        self.session.add(study_dto)
        self.session.flush()
        self.study_id = study_dto.id

        study_content_dto = StudyContentDto(
            study_id=self.study_id,
            page=1,
            content='test content')
        self.session.add(study_content_dto)
        self.session.commit()

    def test_delete_study(self):
        study = Study(
            admin_id=self.admin_id,
            study_cd=self.study_cd)
        self.study_repository.delete(study)
        with self.assertRaises(sqlalchemy.exc.NoResultFound):
            self.session.query(StudyDto).filter(StudyDto.study_cd==self.study_cd).one()

    def test_delete_content(self):
        study = Study(
            admin_id=self.admin_id,
            study_cd=self.study_cd)
        self.study_repository.delete(study)
        with self.assertRaises(sqlalchemy.exc.NoResultFound):
            self.session.query(StudyContentDto).filter(StudyContentDto.study_id==self.study_id).one()

class TestStudyRepositoryFind(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(StudyDto).delete()
        self.session.query(StudyContentDto).delete()
        self.study_repository = StudyRepository(self.session)

        self.admin_id = 1
        self.study_cd = 'test_study'
        self.title = 'test title'

        study_dto = StudyDto(
            admin_id=self.admin_id,
            study_cd =self.study_cd,
            title=self.title)
        self.session.add(study_dto)
        self.session.flush()
        self.study_id = study_dto.id
        self.content = 'test content'

        study_content_dto = StudyContentDto(
            study_id=self.study_id,
            page=1,
            content=self.content)
        self.session.add(study_content_dto)
        self.session.commit()

    def test_title(self):
        study = self.study_repository.find_by_id(self.study_id)

        expected = self.title
        actual = study.get_title()
        self.assertEqual(expected, actual)

    def test_content(self):
        study = self.study_repository.find_by_id(self.study_id)

        expected = self.content
        actual = study.get_contents()[0]
        self.assertEqual(expected, actual)

class TestStudyRepositoryFindAll(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(StudyDto).delete()
        self.session.query(StudyContentDto).delete()
        self.study_repository = StudyRepository(self.session)

        self.admin_id = 1
        self.study_cd1 = 'test_study'
        self.study_cd2 = 'test_study2'

        study_dto1 = StudyDto(
            admin_id=self.admin_id,
            study_cd =self.study_cd1)
        self.session.add(study_dto1)

        study_dto2 = StudyDto(
            admin_id=self.admin_id,
            study_cd =self.study_cd2)
        self.session.add(study_dto2)

        self.session.commit()

    def test_first_element(self):
        studies = self.study_repository.find_all_on_admin(self.admin_id)

        expected = self.study_cd1
        actual = studies.get_studies()[0].get_study_cd()
        self.assertEqual(expected, actual)

    def test_last_element(self):
        studies = self.study_repository.find_all_on_admin(self.admin_id)

        expected = self.study_cd2
        actual = studies.get_studies()[-1].get_study_cd()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()