import unittest
import sys
sys.path.append("..")
from app.models.user import User
from app.models.tanto import Tanto
from resources.data.problem import ProblemData

class TestUserAddTanto(unittest.TestCase):

	def setUp(self):
		self.admin_id = 1
		self.user_id = 1
		self.user_cd = 'user'

	def test_tantos_length(self):
		# arrange
		user = User(
			admin_id=self.admin_id,
			user_cd=self.user_cd)
		tanto1 = Tanto()
		tanto2 = Tanto()

		user.add_tanto(tanto1)
		user.add_tanto(tanto2)

		# assert
		expected = 2
		actual = len(user.get_tantos())
		self.assertEqual(expected, actual)

	def test_tanto_name_of_first_element(self):
		# arrange
		user = User(
			admin_id=self.admin_id,
			user_cd=self.user_cd)
		tanto1 = Tanto()
		tanto1.set_name('tanto1')
		tanto2 = Tanto()
		tanto2.set_name('tanto2')

		user.add_tanto(tanto1)
		user.add_tanto(tanto2)

		# assert
		expected = 'tanto1'
		actual = user.get_tantos()[0].get_name()
		self.assertEqual(expected, actual)

	def test_tanto_name_of_last_element(self):
		# arrange
		user = User(
			admin_id=self.admin_id,
			user_cd=self.user_cd)
		tanto1 = Tanto()
		tanto1.set_name('tanto1')
		tanto2 = Tanto()
		tanto2.set_name('tanto2')

		user.add_tanto(tanto1)
		user.add_tanto(tanto2)

		# assert
		expected = 'tanto2'
		actual = user.get_tantos()[-1].get_name()
		self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()

