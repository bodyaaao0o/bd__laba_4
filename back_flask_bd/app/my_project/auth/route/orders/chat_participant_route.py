from http import HTTPStatus
from flask import Blueprint, jsonify, make_response, request, abort, Response
from back_flask_bd.app.my_project.auth.controller.orders.chat_participant_controler import ChatParticipantController
from back_flask_bd.app.my_project.auth.domain import ChatParticipant

chat_participant_bp = Blueprint('chat_participant', __name__, url_prefix='/chat_participant')

chat_participant_controller_instance = ChatParticipantController()
user_participant_controller_instance = ChatParticipantController()

@chat_participant_bp.route('/', methods=['GET'])
def get_all_chat_participants() -> Response:
    return make_response(jsonify(chat_participant_controller_instance.find_all()), HTTPStatus.OK)

@chat_participant_bp.post('/')
def create_chat_participant() -> Response:
    content = request.get_json()
    chat_participant = ChatParticipant(**content)
    chat_participant_controller_instance.create(chat_participant)
    return make_response(jsonify(chat_participant.put_into_dto()), HTTPStatus.CREATED)

@chat_participant_bp.get('/chat/<int:chat_id>')
def get_chat_participants_by_chat(chat_id: int) -> Response:
    participants = chat_participant_controller_instance.get_chat_participants_by_chat(chat_id)
    if not participants:
        return make_response(jsonify({"error": "No participants found for this chat."}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify(participants), HTTPStatus.OK)

@chat_participant_bp.get('/user/<int:user_id>')
def get_chat_participants_by_user(user_id: int) -> Response:
    participants = user_participant_controller_instance.get_chat_participants_by_user(user_id)
    if not participants:
        return make_response(jsonify({"error": "No participants found for this chat."}), HTTPStatus.NOT_FOUND)
    return make_response(jsonify(participants), HTTPStatus.OK)

@chat_participant_bp.delete('/<int:chat_id>/<int:user_id>')
def delete_chat_participant(chat_id: int, user_id: int) -> Response:
    try:
        chat_participant_controller_instance.delete(chat_id, user_id)
        return make_response(jsonify({"message": "Chat participant deleted successfully."}), HTTPStatus.NO_CONTENT)
    except ValueError as e:
        return make_response(jsonify({"error": str(e)}), HTTPStatus.NOT_FOUND)
    except Exception as e:
        return make_response(jsonify({"error": "An error occurred while deleting the chat participant."}), HTTPStatus.INTERNAL_SERVER_ERROR)
