from __future__ import unicode_literals
from django.db import models
from django.db import connection
from entry_task.exceptions import InsertError
from entry_task.models.activity_manager import ActivityManager


class CommentManager(ActivityManager):
    def get_list_comments(self, eid):
        return [comment.as_json() for comment in self.defer("event_id").filter(event_id=eid)]

    def insert_to_database(self, *query_list):
        query = "INSERT INTO " + self.model._meta.db_table + "(event_id,user_id,date,content) VALUES (%s,%s,%s,%s)"
        cursor = connection.cursor()
        try:
            cursor.execute(query, query_list)
        except Exception as e:
            raise InsertError("Error when inserting into database")

    def get_user_records(self, user_id):
        return [dict(event_id=row.event_id,
                     content=row.content,
                     date=row.date, )
                for row in self.defer("user_id").filter(user_id=user_id)]


class EventComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    user_id = models.IntegerField()
    date = models.IntegerField()
    content = models.CharField(max_length=500)
    objects = CommentManager()

    def as_json(self):
        return dict(
            user_id=self.user_id,
            date=self.date,
            content=self.content,
        )

    class Meta:
        managed = False
        db_table = 'event_comment_tab'

