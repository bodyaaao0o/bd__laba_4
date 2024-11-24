from __future__ import annotations

from datetime import datetime
from typing import Dict, Any

from alembic.util import status

from back_flask_bd.app.my_project.auth.domain.orders.user_status import UserStatus
from back_flask_bd.app.my_project.database import db
from back_flask_bd.app.my_project.auth.domain.i_dto import IDto

class User(db.Model, IDto):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    created_data = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

    user_status_id = db.Column(db.Integer, db.ForeignKey('user_status.id'), nullable=True)
    status = db.relationship("UserStatus", backref="users")

    user_activity_log_id = db.Column(db.Integer, db.ForeignKey('activity_log.id'), nullable=True)
    user_action = db.relationship("ActivityLog", backref="user")


    chats = db.relationship('Chat', secondary='chat_participant', back_populates='users')

    def __repr__(self) -> str:
        return f"User  ('{self.id}', '{self.user_name}', '{self.email}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Представити користувача у вигляді словника, включаючи останню активність.
        """
        # last_activity = self.get_last_activity()
        return {
            "id": self.id,
            "user_name": self.user_name,
            "email": self.email,
            "password": self.password,
            "user_status_id": self.user_status_id if self.user_status_id else None,
            "status": self.status.status if self.status else None,
            "user_activity_log_id": self.user_activity_log_id if self.user_activity_log_id else None,
            "user_action": self.user_action.action if self.user_action else None

            # "last_activity": last_activity
        }

    @classmethod
    def create_from_dto(cls, dto):
        if 'user_name' not in dto or 'email' not in dto:
            raise ValueError("DTO must include 'user_name' and 'email'")
        return cls(**dto)

