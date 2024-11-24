from back_flask_bd.app.my_project.auth.controller.general_controller import GeneralController
from back_flask_bd.app.my_project.auth.service.orders.user_service import UserService


class UserController(GeneralController):

    def __init__(self):
        super().__init__(UserService())  # Ініціалізація конкретного сервісу для користувачів

    def find_by_username(self, username):
        return self._service.find_by_username(username)
