import hashlib
import copy

class User():
	def __init__(self, admin_id, user_cd):
		self.admin_id = admin_id
		self.user_cd = user_cd
		self.user_name = ''
		self.password = ''
		self.mail = ''
		self.tantos = []

	def set_user_name(self, user_name):
		self.user_name = user_name

	def regist_password(self, password):
		# SHA-256でハッシュ化
		self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()

	def add_tanto(self, tanto):
		self.tantos.append(tanto)

	def reset_tanto(self):
		self.tantos = []

	def get_tantos(self):
		return copy.deepcopy(self.tantos)
