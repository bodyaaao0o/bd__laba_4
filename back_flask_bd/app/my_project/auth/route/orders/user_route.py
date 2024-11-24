from http import HTTPStatus
from os import abort

from flask import Blueprint, jsonify, Response, request, make_response

from back_flask_bd.app.my_project import db
from back_flask_bd.app.my_project.auth.controller import user_controller
from back_flask_bd.app.my_project.auth.controller.orders.user_controller import UserController
from back_flask_bd.app.my_project.auth.domain import User
from back_flask_bd.app.my_project.auth.domain.orders.user_status import UserStatus

user_status = UserStatus()

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/', methods=['GET'])
def get_all_users() -> Response:
    user_controller_instance = UserController()
    return make_response(jsonify(user_controller_instance.find_all()), HTTPStatus.OK)


@user_bp.post('/')
def create_user() -> Response:
    content = request.get_json()

    # Отримання статусу з бази даних, щоб встановити user_status_id
    status_id = content.get("user_status_id")
    if status_id:
        user_status = UserStatus.query.get(status_id)
        if not user_status:
            abort(HTTPStatus.BAD_REQUEST, "Invalid user_status_id provided.")

    # Створення нового користувача
    user = User.create_from_dto(content)
    if not user:
        abort(HTTPStatus.BAD_REQUEST, "Invalid data provided for user.")

    db.session.add(user)
    db.session.commit()

    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)


@user_bp.get('/<int:user_id>')
def get_user(user_id: int) -> Response:
    user_controller_instance = UserController()
    user = user_controller_instance.find_by_id(user_id)
    if not user:
        abort(HTTPStatus.NOT_FOUND, f"User with id {user_id} not found.")

    return make_response(jsonify(user_controller_instance.find_by_id(user_id)), HTTPStatus.OK)


@user_bp.put('/<int:user_id>')
def update_user(user_id: int) -> Response:
    content = request.get_json()
    if content is None:
        abort(HTTPStatus.BAD_REQUEST, "No data provided")
    user = User.create_from_dto(content)
    if not user:
        abort(HTTPStatus.BAD_REQUEST, "Invalid data provided for user")
    user_controller_instance = UserController()
    user_controller_instance.update(user_id, user)

    return make_response("User updated", HTTPStatus.OK)

@user_bp.patch('/<int:user_id>')
def patch_user(user_id: int) -> Response:
    content = request.get_json()
    UserController.patch(user_id, content)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.delete('/<int:user_id>')
def delete_user(user_id: int) -> Response:
    user_controller_instance = UserController()
    user_controller_instance.delete(user_id)
    return make_response("User deleted", HTTPStatus.OK)
