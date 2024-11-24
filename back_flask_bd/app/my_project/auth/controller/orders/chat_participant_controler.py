from typing import List
from flask import request

from back_flask_bd.app.my_project.auth.dao.orders.chat_paticipant_dao import ChatParticipantDAO
from back_flask_bd.app.my_project.auth.domain import ChatParticipant
from back_flask_bd.app.my_project.auth.service.orders.chat_paticipant_service import ChatParticipantService
from back_flask_bd.app.my_project.auth.controller.general_controller import GeneralController

class ChatParticipantController(GeneralController):
    def __init__(self):
        chat_participant_dao = ChatParticipantDAO()
        service = ChatParticipantService(chat_participant_dao)
        super().__init__(service)

    def post(self) -> object:
        data = request.get_json()
        chat_participant = ChatParticipant(**data)
        return self.create(chat_participant)

    def get_chat_participants_by_chat(self, key: int) -> List[object]:
        participants = self._service.find_by_chat_id(key)
        return [participant.put_into_dto() for participant in participants]

    def get_chat_participants_by_user(self, key: int) -> List[object]:
        participants = self._service.find_by_user_id(key)
        return [participant.put_into_dto() for participant in participants]

    def delete(self, chat_id: int, user_id: int) -> None:
        try:
            self._service.delete_by_chat_and_user(chat_id, user_id)
        except ValueError as e:
            raise ValueError(str(e))
