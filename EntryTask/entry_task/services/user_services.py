from entry_task.models.user import User
from django.shortcuts import get_list_or_404
from entry_task import settings
from entry_task.models import User, UserActivity, EventLike, EventParticipation, EventComment
from entry_task.exceptions import NotFoundError
jwt_payload_handler = settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = settings.JWT_ENCODE_HANDLER


def login(username, password):
    user = User.authenticate(username,password)
    payload = jwt_payload_handler(user)
    return jwt_encode_handler(payload)


def get_user_by_id(id):
    try:
        user = User.objects.get(pk=id)
        return user.as_json()
    except User.DoesNotExist:
        raise NotFoundError("Cannot find the user")


def get_list_user():
    users = get_list_or_404(User)
    data = [user.as_json() for user in users]
    return data


def get_activities(user_id):
    likes = EventLike.objects.get_user_records(user_id)
    participates = EventParticipation.objects.get_user_records(user_id)
    comments = EventComment.objects.get_user_records(user_id)
    user_activity = UserActivity(likes=likes, participates=participates, comments=comments)
    return user_activity.as_json()


