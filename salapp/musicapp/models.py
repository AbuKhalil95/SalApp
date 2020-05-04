from django.db import models


# Create your models here.
class Artist(models.Model):
    track_name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    # logo_url = models.CharField(max_length=100)

    def __str__(self):
        return self.track_name


# class Album(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     album_text = models.CharField(max_length=100)
#
#
# class Tracks(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     track_text = models.CharField(max_length=100)
