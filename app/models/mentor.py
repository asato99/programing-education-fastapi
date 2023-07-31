import hashlib

class Mentor():
	def __init__(self, admin_id, role, mentor_cd):
		self.admin_id = admin_id
		self.role = role
		self.mentor_cd = mentor_cd
		self.name = ''
		self.mail = ''
		self.password = ''
		self.created_at = ''

	def set_name(self, name):
		self.name = name

	def set_mail(self, mail):
		self.mail = mail

	def set_created_at(self, created_at):
		self.created_at = created_at

	def regist_password(self, password):
		# SHA-256でハッシュ化
		self.password = hashlib.sha256(password.encode("utf-8")).hexdigest()

	def get_admin_id(self):
		return self.admin_id

	def get_role(self):
		return self.role

	def get_mentor_cd(self):
		return self.mentor_cd

	def get_name(self):
		return self.name

	def get_mail(self):
		return self.mail

	def get_created_at(self):
		return self.created_at

	def get_password(self):
		return self.password

	def export(self):
		return {
			'mentor_cd': self.get_mentor_cd(),
			'mentor_name': self.get_name(),
			'role': self.get_role(),
			'created_at': self.get_created_at(),
		}

class Mentors():
	def __init__(self):
		self.mentors = []
	
	def add_mentor(self, mentor):
		self.mentors.append(mentor)
	
	def get_mentors(self):
		return self.mentors
	
	def reset(self):
		self.mentors = []

	def export_headers(self):
		headers = []
		for mentor in self.mentors:
			headers.append(mentor.export())
		return headers
