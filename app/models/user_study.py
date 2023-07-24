class UserStudy():
    def __init__(self, user_id, study):
        self.user_id = user_id
        self.study = study
        self.created_at = ''

    def set_created_at(self, created_at):
        self.created_at = created_at

    def get_created_at(self):
        return self.created_at

    def get_user_id(self):
        return self.user_id

    def get_admin_id(self):
        return self.study.get_admin_id()

    def get_study_cd(self):
        return self.study.get_study_cd()

    def export(self):
        return {
            'study_cd': self.get_study_cd(),
            'title': self.study.get_title(),
            'created_at': self.get_created_at(),
            'updated_at': self.study.get_updated_at(),
        }

class UserStudies():
    def __init__(self):
        self.user_studies = []
        
    def add_user_study(self, user_study):
        self.user_studies.append(user_study)

    def reset_user_studies(self):
        self.user_studies = []

    def export(self):
        items = []
        for user_study in self.user_studies:
            items.append(user_study.export())
        return items