from entry_task.models import User, EventInfo, Event, EventLike, EventParticipation, EventComment, Image
from entry_task.helpers import event_helpers
from entry_task.exceptions import InsertError,NotFoundError


def get_event(event_id):
    try:
        event_info = EventInfo.objects.get(event_id=event_id)
        participants = EventParticipation.objects.get_list_users(event_id)
        likes = EventLike.objects.get_list_users(event_id)
        comments = EventComment.objects.get_list_comments(event_id)
        photos = Image.objects.get_photo_srcs(event_id)
        event = Event(event_info,photos,likes,comments,participants)
        return event.as_json()
    except EventInfo.DoesNotExist:
        raise NotFoundError("Cannot find the event")


def get_list_events(page, page_size, event_type, start_date, end_date):
    events = EventInfo.objects.all()
    events = event_helpers.filter_list_by_type(events, event_type)
    events = event_helpers.filter_list_by_date_ranges(events, start_date, end_date)
    events = event_helpers.paginate_list(events, page, page_size)
    data = [event.as_json() for event in events]
    return data


def insert_activity(event_id, user_id, type, date, content=""):
    if not EventInfo.objects.filter(event_id = event_id).exists() or not User.objects.filter(user_id = user_id).exists():
        raise InsertError("Event or user does not exist")
    if type == "comments":
        EventComment.objects.insert_to_database(event_id, user_id, date, content)
    elif type == "likes":
        EventLike.objects.insert_to_database(event_id, user_id, date)
    else:
        EventParticipation.objects.insert_to_database(event_id, user_id, date)
