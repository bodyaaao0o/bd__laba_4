from typing import List
from back_flask_bd.app.my_project.auth.domain import UserStatus
from back_flask_bd.app.my_project.auth.dao.general_dao import GeneralDao

class UserStatusDAO(GeneralDao):

    _domain_type = UserStatus



