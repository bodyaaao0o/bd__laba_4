from abc import ABC
from typing import List
from back_flask_bd.app.my_project.database import db
from sqlalchemy import inspect
from sqlalchemy.orm import Mapper




class GeneralDao(ABC):
    _domain_type = None
    _session = db.session


    def find_all(self):
        return self._session.query(self._domain_type).all()

    def find_by_id(self, key: int) -> object:

        return self._session.query(self._domain_type).get(key)

    def create(self, obj: object) -> object:

        self._session.add(obj)
        self._session.commit()
        return obj

    def create_all(self, objs: List[object]) -> List[object]:
        self._session.add_all(objs)
        self._session.commit()
        return objs

    def update(self, key: int, in_obj: object) -> None:
        domain_obj = self._session.query(self._domain_type).get(key)
        if domain_obj is None:
            raise ValueError("Object not found")

        mapper = inspect(self._domain_type)
        columns = mapper.columns

        # Оновлення атрибутів
        for column in columns:
            if not column.primary_key:
                value = getattr(in_obj, column.name)
                setattr(domain_obj, column.name, value)

        self._session.commit()

    def patch(self, key: int, field_name: str, value: object) -> None:
        domain_obj = self._session.query(self._domain_type).get(key)
        setattr(domain_obj, field_name, value)  # Заміна значення поля
        self._session.commit()

    def delete(self, key: int) -> None:
        domain_obj = self._session.query(self._domain_type).get(key)
        if domain_obj is None:
            raise ValueError("Object not found")
        self._session.delete(domain_obj)
        try:
            self._session.commit()
        except Exception as e:
            self._session.rollback()
            raise RuntimeError(f"Error while deleting object: {e}")

    def delete_all(self) -> None:

        self._session.query(self._domain_type).delete()
        self._session.commit()
