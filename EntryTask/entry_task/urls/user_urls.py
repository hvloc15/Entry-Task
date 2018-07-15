from django.conf.urls import url
from entry_task.views import user

urlpatterns = [
    url(r'^login$', user.login, name="user_login"),
    url(r'^$', user.get_list_users, name="get_list_users"),
    url(r'^(?P<user_id>[0-9]+)$', user.get_user, name="get_user"),
    url(r'^(?P<user_id>[0-9]+)/activities$', user.get_activities, name="get_user_activities"),
]