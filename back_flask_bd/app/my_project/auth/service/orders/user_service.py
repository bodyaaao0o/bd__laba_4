from back_flask_bd.app.my_project.auth.dao.orders.user_dao import UserDAO
from back_flask_bd.app.my_project.auth.service.general_service import GeneralService


class UserService(GeneralService):
    def __init__(self):
        super().__init__(UserDAO())

    def find_by_username(self, username):
        return self._dao.find_by_username(username)