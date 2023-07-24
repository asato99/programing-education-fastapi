class Study():
	def __init__(self, admin_id, study_cd):
		self.admin_id = admin_id
		self.study_cd = study_cd
		self.title = ''
		self.contents = []
		self.created_at = ''
		self.updated_at = ''

	def set_title(self, title):
		self.title = title

	def set_created_at(self, created_at):
		self.created_at = created_at

	def set_updated_at(self, updated_at):
		self.updated_at = updated_at

	def set_title(self, title):
		self.title = title

	def get_admin_id(self):
		return self.admin_id

	def get_study_cd(self):
		return self.study_cd

	def get_title(self):
		return self.title

	def get_created_at(self):
		return self.created_at

	def get_updated_at(self):
		return self.updated_at

	def add_content(self, content):
		self.contents.append(content)
	
	def reset_contents(self):
		self.contents = []

	def get_contents(self):
		return self.contents

class Studies():
	def __init__(self):
		self.studies = []

	def add_study(self, study):
		self.studies.append(study)

	def export(self):
		return self.studies
