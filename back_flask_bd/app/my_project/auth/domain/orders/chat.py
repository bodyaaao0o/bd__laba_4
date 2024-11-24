from __future__ import annotations
from datetime import datetime
from typing import Dict, Any
from back_flask_bd.app.my_project.database import db
from back_flask_bd.app.my_project.auth.domain.i_dto import IDto
# db = SQLAlchemy()


class Chat(db.Model, IDto):
    __tablename__ = 'chat'

    id = db.Column(db.Integer, primary_key=True)
    chat_name = db.Column(db.String(45), nullable=False)
    created_chat = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)
    users = db.relationship('User', secondary='chat_participant', back_populates='chats')

    def __repr__(self) -> str:
        return f"Chat('{self.id}', '{self.chat_name}', '{self.created_chat}')"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "chat_name": self.chat_name,
            "created_chat": self.created_chat,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Chat:
        return Chat(**dto_dict)