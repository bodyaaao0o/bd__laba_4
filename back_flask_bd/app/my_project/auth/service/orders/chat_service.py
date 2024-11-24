from back_flask_bd.app.my_project.auth.dao.orders.chat_dao import ChatDAO
from back_flask_bd.app.my_project.auth.service.general_service import GeneralService


class ChatService(GeneralService):
    def __init__(self):
        super().__init__(ChatDAO())

    def find_by_chat_name(self, chat_name):
        return self._dao.find_by_chat_name(chat_name)