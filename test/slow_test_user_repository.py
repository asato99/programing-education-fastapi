
import unittest
import os
import sys
import sqlalchemy
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.models.tanto import Tanto
from app.db.tables import UserDto, TantoDto
from resources.db import setting

class TestUserRepositoryRegist(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserDto).delete()
        self.session.query(TantoDto).delete()
        self.user_repository = UserRepository(self.session)

        self.admin_id = 1
        self.user_id = 1
        self.user_cd = 'user'
        self.user_name = 'user_name'

    # @unittest.skip("temporary test")
    def test_regist(self):
        # arrange
        user = User(
            admin_id=self.admin_id,
            user_cd=self.user_cd
        )
        user.set_name(self.user_name)
        tanto1 = Tanto()
        tanto1.set_name('tanto1')
        tanto1.set_mail('tanto1_mail')
        user.add_tanto(tanto1)

        tanto2 = Tanto()
        tanto2.set_name('tanto2')
        tanto2.set_mail('tanto2_mail')
        user.add_tanto(tanto2)

        self.user_repository.regist(user)

        user_dto = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd).first()
        expected = self.user_name
        actual = user_dto.user_name
        self.assertEqual(expected, actual)

class TestUserRepositorySave(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserDto).delete()
        self.session.query(TantoDto).delete()
        self.user_repository = UserRepository(self.session)

        self.admin_id = 1
        self.user_cd = 'user'
        self.user_name = 'user_name'
        self.update_name = 'user_name_update'

        user_dto = UserDto(
            admin_id=self.admin_id,
            user_cd=self.user_cd,
            user_name=self.user_name)
        tanto_dto = TantoDto(
            name='tanto1',
            mail='tanto1mail'
        )
        self.session.add(user_dto)
        self.session.add(tanto_dto)
        self.session.commit()

        user = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd).first()
        self.user_id = user.user_id

    def test_save(self):
        user = User(
            admin_id=self.admin_id,
            user_cd=self.user_cd
        )
        user.set_user_id(self.user_id)
        user.set_name(self.update_name)
        tanto1 = Tanto()
        tanto1.set_name('tanto1_update')
        tanto1.set_mail('tanto1_mail_update')
        user.add_tanto(tanto1)

        tanto2 = Tanto()
        tanto2.set_name('tanto2_update')
        tanto2.set_mail('tanto2_mail_update')
        user.add_tanto(tanto2)

        self.user_repository.save(user)

        user_dto = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd).first()
        expected = self.update_name
        actual = user_dto.user_name
        self.assertEqual(expected, actual)

class TestUserRepositoryDelete(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserDto).delete()
        self.session.query(TantoDto).delete()
        self.user_repository = UserRepository(self.session)

        self.admin_id = 1
        self.user_id = 1
        self.user_cd = 'user'
        self.user_name = 'user_name'

        user_dto = UserDto(
            admin_id=self.admin_id,
            user_cd=self.user_cd,
            user_name=self.user_name)
        tanto_dto = TantoDto(
            name='tanto1',
            mail='tanto1mail'
        )
        self.session.add(user_dto)
        self.session.add(tanto_dto)
        self.session.commit()

        user = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd).first()
        self.user_id = user.user_id

    def test_user_deleted(self):
        user = User(
            admin_id=self.admin_id,
            user_cd=self.user_cd
        )
        user.set_user_id(self.user_id)
        tanto1 = Tanto()
        user.add_tanto(tanto1)

        tanto2 = Tanto()
        user.add_tanto(tanto2)

        self.user_repository.delete(user)
        with self.assertRaises(sqlalchemy.exc.NoResultFound):
            self.session.query(UserDto).filter(UserDto.user_id==self.user_id).one()

    def test_tantos_deleted(self):
        user = User(
            admin_id=self.admin_id,
            user_cd=self.user_cd
        )
        user.set_user_id(self.user_id)
        tanto1 = Tanto()
        user.add_tanto(tanto1)

        tanto2 = Tanto()
        user.add_tanto(tanto2)

        self.user_repository.delete(user)
        with self.assertRaises(sqlalchemy.exc.NoResultFound):
            self.session.query(TantoDto).filter(TantoDto.user_id==self.user_id).one()

class TestUserRepositoryFind(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserDto).delete()
        self.session.query(TantoDto).delete()
        self.user_repository = UserRepository(self.session)

        self.admin_id = 1
        self.user_id = 1
        self.user_cd = 'user'
        self.user_name = 'user_name'

        self.tanto_name = 'tanto'
        self.tanto_mail = 'tanto_mail'

        user_dto = UserDto(
            admin_id=self.admin_id,
            user_cd=self.user_cd,
            user_name=self.user_name)
        self.session.add(user_dto)
        self.session.commit()

        user = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd).first()
        self.user_id = user.user_id

        tanto_dto = TantoDto(
            user_id=self.user_id,
            name=self.tanto_name,
            mail=self.tanto_mail
        )
        self.session.add(tanto_dto)
        self.session.commit()

    def test_user_name(self):
        user = self.user_repository.find_by_id(self.user_id)

        expected = self.user_name
        actual = user.get_name()
        self.assertEqual(expected, actual)

    def test_tanto_name(self):
        user = self.user_repository.find_by_id(self.user_id)

        expected = self.tanto_name
        actual = user.get_tantos()[0].get_name()
        self.assertEqual(expected, actual)

class TestUserRepositoryFindAll(unittest.TestCase):
    def setUp(self):
        # self.skipTest("depends on db")
        self.session = setting.get_session()
        self.session.query(UserDto).delete()
        self.session.query(TantoDto).delete()
        self.user_repository = UserRepository(self.session)

        self.admin_id = 1

        self.user_id1 = 1
        self.user_id2 = 2

        self.user_cd1 = 'user1'
        self.user_cd2 = 'user2'

        self.user_name1 = 'user_name'
        self.user_name2 = 'user_name'

        user_dto1 = UserDto(
            admin_id=self.admin_id,
            user_cd=self.user_cd1,
            user_name=self.user_name1)
        user_dto2 = UserDto(
            admin_id=self.admin_id,
            user_cd=self.user_cd2,
            user_name=self.user_name2)

        self.session.add(user_dto1)
        self.session.add(user_dto2)
        self.session.commit()

        user1 = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd1).first()
        user2 = self.session.query(UserDto).filter(UserDto.user_cd==self.user_cd2).first()
        self.user_id1 = user1.user_id
        self.user_id2 = user2.user_id

        self.tanto_name1 = 'tanto1'
        self.tanto_mail1 = 'tanto_mail1'
        tanto_dto1 = TantoDto(
            user_id=self.user_id1,
            name=self.tanto_name1,
            mail=self.tanto_mail1
        )
        self.session.add(tanto_dto1)

        self.tanto_name2 = 'tanto2'
        self.tanto_mail2 = 'tanto_mail2'
        tanto_dto2 = TantoDto(
            user_id=self.user_id2,
            name=self.tanto_name2,
            mail=self.tanto_mail2
        )
        self.session.add(tanto_dto2)

        self.session.commit()

    def test_headers_length(self):
        users = self.user_repository.find_all(self.admin_id)
        headers = users.export_headers()

        expected = 2
        actual = len(headers)
        self.assertEqual(expected, actual)

    def test_first_element_of_headers(self):
        users = self.user_repository.find_all(self.admin_id)
        headers = users.export_headers()

        expected = self.user_name1 
        actual = headers[0]['user_name'] 
        self.assertEqual(expected, actual)

    def test_last_element_of_headers(self):
        users = self.user_repository.find_all(self.admin_id)
        headers = users.export_headers()

        expected = self.user_name2 
        actual = headers[-1]['user_name'] 
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()