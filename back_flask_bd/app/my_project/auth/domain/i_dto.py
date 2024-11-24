from abc import abstractmethod

from typing import Dict


class IDto:

    @abstractmethod
    def put_into_dto(self) -> Dict[str, object]:
        """
        :return:
        """
    @staticmethod
    @abstractmethod
    def create_from_dto(dto_dict: Dict[str, object]) -> object:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """

