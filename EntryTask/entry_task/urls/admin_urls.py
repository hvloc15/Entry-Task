from django.conf.urls import url
from entry_task.views import admin

urlpatterns = [
    url(r'^$', admin.admin_page, name="admin_page"),
    url(r'^login/$',admin.login, name="admin_login_page"),
    url(r'^logout/$',admin.logout, name="admin_logout_page"),
]