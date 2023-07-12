from app.types.user import UserInfo
from app.models.tanto import Tanto

class UserService():

    @classmethod
    def set_info(cls, user, user_info: UserInfo):
        user.set_cd(user_info.user_cd)
        user.set_name(user_info.user_name)

        if user_info.mail != '':
            user.set_mail(user_info.mail)

        for tanto_info in user_info.tantos:
            tanto = Tanto()
            tanto.set_name(tanto_info.name)
            tanto.set_mail(tanto_info.mail)
            user.add_tanto(tanto)
    