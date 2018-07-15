from __future__ import unicode_literals
from entry_task.exceptions import AuthenticationFailed
from django.db import models
import hashlib

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)
    username = models.CharField(unique=True, max_length=100)
    password = models.CharField(max_length=100)

    @staticmethod
    def authenticate(username, password):
        try:
            user = User.objects.get(username=username)
            if user.password != hashlib.md5(password).hexdigest():
                raise AuthenticationFailed()
            return user
        except User.DoesNotExist:
            raise AuthenticationFailed

    @staticmethod
    def authenticate_payload(payload):
        try:
            id = payload.get('user_id')
            if id:
                user = User.objects.only('user_id').get(user_id=id)
            else:
                raise AuthenticationFailed("Invalid payload")
        except User.DoesNotExist:
            raise AuthenticationFailed("User does not exist")
        return user

    def as_json(self):
        return dict(
            id=self.user_id,
            username=self.username,
            role=self.role,
        )

    class Meta:
        managed = False
        db_table = 'user_info_tab'