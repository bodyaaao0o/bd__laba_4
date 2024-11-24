from typing import List

from back_flask_bd.app.my_project.auth.dao.general_dao import GeneralDao
from back_flask_bd.app.my_project.auth.domain import User
import sqlalchemy

class UserDAO(GeneralDao):

    _domain_type = User

    def find_by_username(self, username: str) -> List[object]:
        return self._session.query(User).filter(User.username == username).order_by(User.username).all()

    @staticmethod
    def find_users_by_status(user_status_id: int):
        return User.query.filter_by(user_status_id=user_status_id).all()

    @staticmethod
    def get_users_by_action(user_activity_log_id: int):
        return User.query.filter_by(user_activity_log_id=user_activity_log_id).all()