from http import HTTPStatus
from os import abort

from flask import Blueprint, jsonify, Response, request, make_response
from back_flask_bd.app.my_project.auth.controller import chat_controller  # Імпортуйте ваш контролер
from back_flask_bd.app.my_project.auth.domain.orders.chat import Chat  # Імпортуйте вашу модель Chat

chat_bp = Blueprint('chat', __name__, url_prefix='/chat')

@chat_bp.route('/', methods=['GET'])
def get_all_chats() -> Response:
    chat_controller_instance = chat_controller()
    return make_response(jsonify(chat_controller_instance.find_all()), HTTPStatus.OK)

@chat_bp.post('/')
def create_chat() -> Response:
    content = request.get_json()

    # Створіть об'єкт моделі Chat безпосередньо з отриманого контенту
    chat = Chat.create_from_dto(content)  # Припустимо, що create_chat повертає екземпляр Chat

    # Тепер передайте екземпляр моделі до контролера
    chat_controller_instance = chat_controller()
    chat_controller_instance.create(chat)  # Передайте об'єкт моделі, а не словник

    return make_response(jsonify(chat.put_into_dto()), HTTPStatus.CREATED)

@chat_bp.get('/<int:chat_id>')
def get_chat(chat_id: int) -> Response:
    chat_controller_instance = chat_controller()
    return make_response(jsonify(chat_controller_instance.find_by_id(chat_id)), HTTPStatus.OK)

@chat_bp.put('/<int:chat_id>')
def update_chat(chat_id: int) -> Response:
    content = request.get_json()

    if content is None:
        abort(HTTPStatus.BAD_REQUEST, "No data provided")

    # Переконайтеся, що ви створюєте об'єкт правильно
    chat = Chat.create_from_dto(content)  # Переконайтеся, що метод create_from_dto правильно працює

    chat_controller_instance = chat_controller()
    chat_controller_instance.update(chat_id, chat)  # Передайте екземпляр моделі

    return make_response(chat.put_into_dto(),"Chat  updated", HTTPStatus.OK)

@chat_bp.patch('/<int:chat_id>')
def patch_chat(chat_id: int) -> Response:
    content = request.get_json()
    chat_controller_instance = chat_controller()
    chat_controller_instance.patch(chat_id, content)  # Передайте часткові дані
    return make_response("Chat updated", HTTPStatus.OK)

@chat_bp.delete('/<int:chat_id>')
def delete_chat(chat_id: int) -> Response:
    chat_controller_instance = chat_controller()
    chat_controller_instance.delete(chat_id)
    return make_response("Chat deleted", HTTPStatus.OK)