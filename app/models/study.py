class Study():
	def __init__(self, admin_id, study_cd):
		self.admin_id = admin_id
		self.study_cd = study_cd
		self.title = ''
		self.contents = []

	def set_title(self, title):
		self.title = title

	def get_admin_id(self):
		return self.admin_id

	def get_study_cd(self):
		return self.study_cd

	def get_title(self):
		return self.title

	def add_content(self, content):
		self.contents.append(content)

	def get_contents(self):
		return self.contents

class Studies():
	def __init__(self):
		self.studies = []

	def add_study(self, study):
		self.studies.append(study)

	def get_studies(self):
		return self.studies
