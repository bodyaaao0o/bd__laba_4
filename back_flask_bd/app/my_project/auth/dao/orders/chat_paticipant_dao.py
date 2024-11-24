from typing import List

import logging
from back_flask_bd.app.my_project.auth.domain import ChatParticipant
from back_flask_bd.app.my_project.auth.dao.general_dao import GeneralDao

class ChatParticipantDAO(GeneralDao):
    _domain_type = ChatParticipant

    def create(self, chat_participant: ChatParticipant) -> None:
        logging.info(
            f"Creating ChatParticipant with user_id={chat_participant.user_id}, chat_id={chat_participant.chat_id}")
        if chat_participant.user_id is None or chat_participant.chat_id is None:
            raise ValueError("user_id and chat_id cannot be None")
        self._session.add(chat_participant)
        self._session.commit()

    def find_by_chat_id(self, chat_id: int) -> List[object]:
        return self._session.query(ChatParticipant).filter(ChatParticipant.chat_id == chat_id).all()

    def find_by_user_id(self, user_id: int) -> List[object]:
        return self._session.query(ChatParticipant).filter(ChatParticipant.user_id == user_id).all()

    def delete_by_chat_and_user(self, chat_key: int, user_key: int) -> None:
        chat_participant = self._session.query(ChatParticipant).filter_by(chat_id=chat_key, user_id=user_key).first()
        if chat_participant:
            self._session.delete(chat_participant)
        else:
            raise ValueError("ChatParticipant not found")