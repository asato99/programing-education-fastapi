
import unittest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from app.repositories.user_repository import UserRepository
from app.models.user import User
from app.models.tanto import Tanto
from app.db.tables import UserDto, TantoDto
from resources.db import setting

class TestProblemRepositoryRegist(unittest.TestCase):
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
            user_id=self.user_id
        )
        user.set_cd(self.user_cd)
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

if __name__ == "__main__":
    unittest.main()