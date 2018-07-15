from __future__ import unicode_literals
from django.db import models


class ImageManager(models.Manager):

    def get_photo_srcs(self,eid):
        return [row.src for row in self.only("src").filter(event_id=eid)]


class Image(models.Model):
    photo_id = models.AutoField(primary_key=True)
    event_id = models.IntegerField()
    src = models.ImageField(max_length=500, upload_to="images/")

    objects = ImageManager()
    class Meta:
        managed = False
        db_table = 'photo_of_event_tab'
