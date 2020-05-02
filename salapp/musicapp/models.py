from django.db import models


# Create your models here.
class music(models.Model):
    track_name = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)

    def __str__(self):
        return self.track_name
