from __future__ import unicode_literals
from entry_task.models.activity_manager import ActivityManager
from django.db import models


class EventLike(models.Model):
    event_id = models.IntegerField(primary_key=True)
    user_id = models.IntegerField(primary_key=True)
    date = models.IntegerField()
    objects = ActivityManager()

    class Meta:
        managed = False
        db_table = 'event_like_tab'
