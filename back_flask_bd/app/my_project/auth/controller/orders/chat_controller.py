from back_flask_bd.app.my_project.auth.controller.general_controller import GeneralController
from back_flask_bd.app.my_project.auth.service.orders.chat_service import ChatService


class ChatController(GeneralController):

    def __init__(self):
        super().__init__(ChatService())  # Ініціалізація конкретного сервісу для користувачів

    def find_by_chat_name(self, chat_name):
        return self._service.find_by_chat_name(chat_name)
