from typing import List

from back_flask_bd.app.my_project.auth.dao.general_dao import GeneralDao
from back_flask_bd.app.my_project.auth.domain import Chat
import sqlalchemy

class ChatDAO(GeneralDao):

    _domain_type = Chat

    def find_by_chat_name(self, chat_name: str) -> List[object]:
        return self._session.query(Chat).filter(Chat.username == chat_name).order_by(Chat.chat_name).all()