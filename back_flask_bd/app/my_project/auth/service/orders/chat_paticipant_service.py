from typing import List
from back_flask_bd.app.my_project.auth.domain import ChatParticipant
from back_flask_bd.app.my_project.auth.dao.orders.chat_paticipant_dao import ChatParticipantDAO

class ChatParticipantService:
    def __init__(self, dao: ChatParticipantDAO):
        self._dao = dao

    def find_by_chat_id(self, chat_id: int) -> List[ChatParticipant]:
        return self._dao.find_by_chat_id(chat_id)

    def find_by_user_id(self, user_id: int) -> List[ChatParticipant]:
        return self._dao.find_by_user_id(user_id)

    def create(self, chat_participant: ChatParticipant) -> ChatParticipant:
        if chat_participant.user_id is None or chat_participant.chat_id is None:
            raise ValueError("user_id and chat_id cannot be None")
        self._dao.create(chat_participant)
        return chat_participant

    def delete_by_chat_and_user(self, chat_key: int, user_key: int) -> None:
        self._dao.delete_by_chat_and_user(chat_key, user_key)

    def find_all(self) -> List[ChatParticipant]:
        return self._dao.find_all()