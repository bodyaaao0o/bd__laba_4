
from .orders.user_dao import UserDAO
from .orders.chat_dao import ChatDAO
from .orders.chat_paticipant_dao import ChatParticipantDAO
from .orders.user_status_dao import UserStatus
from .orders.activity_log_dao import ActivityLogDao

user_dao = UserDAO
chat_dao = ChatDAO
chat_paticipant_dao = ChatParticipantDAO
user_status_dao = UserStatus
activity_log_dao = ActivityLogDao