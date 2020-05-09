from django.db import models


# Create your models here.
class Artist(models.Model):
    track_name = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    logo_url = models.URLField(max_length=350, blank=True)

    def __str__(self):
        return self.artist

# Future implementation for relationship many to one of songs to albums and artists

# class Album(models.Model):
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
#     album_text = models.CharField(max_length=100)
#
#
# class Tracks(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     track_text = models.CharField(max_length=100)
