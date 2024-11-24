from __future__ import annotations

from datetime import datetime
from typing import Dict, Any
from back_flask_bd.app.my_project.database import db
from back_flask_bd.app.my_project.auth.domain.i_dto import IDto

class ChatParticipant(db.Model, IDto):
    __tablename__ = "chat_participant"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    joined_at_chat = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chat.id', ondelete='CASCADE'), nullable=False)

    def __repr__(self) -> str:
        return f"ChatParticipant({self.id}, {self.user_id}, {self.chat_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_id": self.user_id,
            "chat_id": self.chat_id
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> ChatParticipant:
        return ChatParticipant(**dto_dict)
