from .orders.user_service import UserService
from .orders.chat_service import ChatService
from .orders.chat_paticipant_service import ChatParticipantService
from .orders.user_status_service import UserStatusService
from .orders.activity_log_service import ActivityLogService


user_service = UserService
chat_service = ChatService
chat_paticipant_service = ChatParticipantService
user_status_service = UserStatusService
activity_log_service = ActivityLogService