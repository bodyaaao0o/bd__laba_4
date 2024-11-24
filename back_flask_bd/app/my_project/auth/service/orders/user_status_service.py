from typing import Dict, Any

from back_flask_bd.app.my_project.auth.dao.orders.user_dao import UserDAO
from back_flask_bd.app.my_project.auth.dao.orders.user_status_dao import UserStatusDAO
from back_flask_bd.app.my_project.auth.service.general_service import GeneralService


class UserStatusService(GeneralService):
    def __init__(self):
        super().__init__(UserStatusDAO())

    def get_users_by_status(self, user_status_id: int) -> Dict[str, Any]:
        user_status_dao = UserStatusDAO()  # Create an instance
        user_status = user_status_dao.find_by_id(user_status_id)  # Call the method on the instance
        if not user_status:
            raise ValueError("User status not found.")

        users = [user.put_into_dto() for user in UserDAO().find_users_by_status(user_status_id)]
        return {
            "user_status": user_status.put_into_dto(),
            "users": users
        }
