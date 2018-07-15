# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import connection
from entry_task.exceptions import InsertError
from django.db import models
import uuid


class SessionManager(models.Manager):
    def generate_session_id(self):
        session_id = str(uuid.uuid4())
        while self.filter(session_id=session_id).exists():
            session_id = str(uuid.uuid4())
        return session_id

    def create_session(self, username):
        session_id = self.generate_session_id()
        query_list = [session_id, username]
        query = "INSERT INTO " + self.model._meta.db_table + "(session_id,username) VALUES (%s,%s)"
        cursor = connection.cursor()
        try:
            cursor.execute(query, query_list)
            return session_id
        except Exception as e:
            raise InsertError("Error when inserting session_id into database")

    def delete_session(self, session_id):
        query_list = [session_id]
        query = "DELETE FROM " + self.model._meta.db_table + " WHERE session_id = %s"
        cursor = connection.cursor()
        cursor.execute(query, query_list)


# Create your models here.
class Session(models.Model):
    session_id = models.CharField(primary_key=True, max_length=50)
    username = models.CharField(max_length=100)
    objects = SessionManager()
    class Meta:
        managed = False
        db_table = 'session_tab'
