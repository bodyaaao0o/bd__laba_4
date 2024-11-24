from back_flask_bd.app.my_project.auth.controller.general_controller import GeneralController
from back_flask_bd.app.my_project.auth.service.orders.user_status_service import UserStatusService


class UserStatusController(GeneralController):

    def __init__(self):
        super().__init__(UserStatusService())

    def find_users_by_status(self, user_status_id: int):
        return UserStatusService().get_users_by_status(user_status_id)

