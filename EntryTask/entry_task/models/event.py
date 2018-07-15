from __future__ import unicode_literals
from django.db import models
from entry_task.helpers import datetime_helpers

class EventInfo(models.Model):
    event_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=50)
    description = models.CharField(max_length=500, blank=True, null=True)
    date = models.IntegerField()
    location = models.CharField(max_length=100)

    @classmethod
    def create(cls, title, type, description, date, location):
        event_info = cls(title=title,
                         type=type,
                         description=description,
                         date=date,
                         location=location
                         )
        return event_info

    def as_json(self):
        return dict(
            event_id=self.event_id,
            title=self.title,
            description=self.description,
            type=self.type,
            date=self.date,
            location=self.location,
        )

    class Meta:
        managed = False
        db_table = 'event_info_tab'


class Event(object):
    def __init__(self,event_info, photos=[], likes=[], comments=[], participants=[]):
        self.event_info = event_info
        self.photos = photos
        self.likes = likes
        self.comments = comments
        self.participants = participants

    def as_json(self):
        return dict(
            self.event_info.as_json(),
            photos=self.photos,
            likes=self.likes,
            comments=self.comments,
            participants=self.participants,
        )