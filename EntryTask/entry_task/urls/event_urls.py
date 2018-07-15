from django.conf.urls import url
from entry_task.views import event

urlpatterns = [
    url(r'^(?P<event_id>[0-9]+)$', event.get_event, name="get_event"),
    url(r'^$', event.get_list_events, name="get_list_events"),
    url(r'^(?P<event_id>[0-9]+)/likes$', event.handle_activity, name="like_event"),
    url(r'^(?P<event_id>[0-9]+)/comments', event.handle_activity, name="comment_event"),
    url(r'^(?P<event_id>[0-9]+)/participates', event.handle_activity, name="participate_event"),
]