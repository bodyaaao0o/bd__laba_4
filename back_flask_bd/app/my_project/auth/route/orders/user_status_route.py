from http import HTTPStatus
from os import abort

from flask import Blueprint, jsonify, Response, request, make_response

from back_flask_bd.app.my_project import db
from back_flask_bd.app.my_project.auth.controller import user_status_controller
from back_flask_bd.app.my_project.auth.controller.orders.user_status_controller import UserStatusController
from back_flask_bd.app.my_project.auth.domain import UserStatus

user_status_bp = Blueprint('user_status', __name__, url_prefix='/user_status')

@user_status_bp.get('/')
def get_all_user_status() -> Response:
    try:
        user_status_controller_instance = UserStatusController()
        statuses = user_status_controller_instance.find_all()
        print("Знайдені статуси:", statuses)
        return make_response(jsonify(statuses), HTTPStatus.OK)
    except Exception as e:
        print("Помилка при отриманні статусів:", str(e))
        return make_response(jsonify({"error": "Не вдалося отримати статуси"}), HTTPStatus.INTERNAL_SERVER_ERROR)

@user_status_bp.post('/')
def create_user_status() -> Response:
    content = request.get_json()
    user_status = UserStatus.create_from_dto(content)
    db.session.add(user_status)
    db.session.commit()
    return make_response(jsonify(user_status.put_into_dto()), HTTPStatus.CREATED)

@user_status_bp.get('/<int:user_status_id>')
def get_user_status(user_status_id: int) -> Response:
    user_status_controller_instance = UserStatusController()
    return make_response(jsonify(user_status_controller_instance.find_by_id(user_status_id)), HTTPStatus.OK)

@user_status_bp.put('/<int:user_status_id>')
def update_user_status(user_status_id: int) -> Response:
    content = request.get_json()
    if content is None:
        abort(HTTPStatus.BAD_REQUEST, "No data provided")
    user_status = UserStatus.create_from_dto(content)
    user_status_controller_instance = UserStatusController()  # Створюємо екземпляр контролера
    user_status_controller_instance.update(user_status_id, user_status)
    return make_response("User status updated", HTTPStatus.OK)

@user_status_bp.patch('/<int:user_status_id>')
def patch_user_status(user_status_id: int) -> Response:
    content = request.get_json()
    user_status_controller_instance = UserStatusController()
    user_status_controller_instance.patch(user_status_id, content)
    return make_response("User status updated", HTTPStatus.OK)

@user_status_bp.delete('/<int:user_status_id>')
def delete_user_status(user_status_id: int) -> Response:
    user_status_controller_instance = UserStatusController()  # Створюємо екземпляр контролера
    user_status_controller_instance.delete(user_status_id)
    return make_response("User status deleted", HTTPStatus.OK)

@user_status_bp.get('/<int:user_status_id>/user')
def get_users_by_status(user_status_id: int) -> Response:
    user_status_controller_instance = UserStatusController()
    try:
        data = user_status_controller_instance.find_users_by_status(user_status_id)
        return make_response(jsonify(data), HTTPStatus.OK)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND)

