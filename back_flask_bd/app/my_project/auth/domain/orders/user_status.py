from __future__ import annotations
from datetime import datetime
from enum import unique
from typing import Dict, Any
from back_flask_bd.app.my_project.database import db
from back_flask_bd.app.my_project.auth.domain.i_dto import IDto

class UserStatus(db.Model, IDto):
    __tablename__ = 'user_status'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(45),unique=False, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=True)

    # user = db.relationship('User', backref='user_status', lazy='dynamic')

    def __repr__(self) -> str:
        return f"User Status ('{self.id}', '{self.status}', '{self.updated_at}')"

    def put_into_dto(self):
        return {
            'id': self.id,
            'status': self.status
        }

    @staticmethod
    def create_from_dto(dto: dict):
        return UserStatus(**dto)