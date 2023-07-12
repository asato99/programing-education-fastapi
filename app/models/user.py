import hashlib
import copy

class User():
	def __init__(self, admin_id, user_cd):
		self.user_id = 0
		self.admin_id = admin_id
		self.user_cd = user_cd
		self.user_name = ''
		self.password = ''
		self.mail = ''
		self.tantos = []
		self.created_at = ''

	def set_admin_id(self, admin_id):
		self.admin_id = admin_id

	def set_user_id(self, user_id):
		self.user_id = user_id

	def set_cd(self, user_cd):
		self.user_cd = user_cd

	def set_name(self, user_name):
		self.user_name = user_name

	def set_mail(self, mail):
		self.mail = mail

	def set_created_at(self, created_at):
		self.created_at = created_at

	def set_password(self, password):
		self.password = password

	def get_admin_id(self):
		return self.admin_id

	def get_user_id(self):
		return self.user_id

	def get_cd(self):
		return self.user_cd

	def get_name(self):
		return self.user_name

	def get_mail(self):
		return self.mail

	def get_created_at(self):
		return self.created_at

	def get_password(self):
		return self.password

	def regist_password(self, password):
		# SHA-256でハッシュ化
		self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()

	def add_tanto(self, tanto):
		self.tantos.append(tanto)

	def reset_tantos(self):
		self.tantos = []

	def get_tantos(self):
		return copy.deepcopy(self.tantos)

	def export_header(self):
		return {
			'user_id': self.get_user_id(),
			'user_cd': self.get_cd(),
			'user_name': self.get_name(),
            'created_at': format(self.get_created_at(), '%Y年%m月%d日'),
            'accessed_at': format(self.get_created_at(), '%Y/%m/%d %H:%M'),
		}

class Users():
	def __init__(self, admin_id):
		self.admin_id = admin_id
		self.users = []

	def add_user(self, user):
		self.users.append(user)

	def reset_users(self):
		self.users = []

	def export_headers(self):
		headers = []
		for user in self.users:
			headers.append(user.export_header())
		return headers