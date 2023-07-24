from app.models.study import Study
from app.types.study import StudyInfo

class StudyService():
    @classmethod
    def set_study_info(cls, study, study_info:StudyInfo):
        study.set_title(study_info.title)

        study.reset_contents()
        for content in study_info.contents:
            study.add_content(content)
        
