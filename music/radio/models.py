from django.db import models


class Playlist(models.Model):
    title = models.CharField(max_length=200, unique=True)
    play_count = models.IntegerField(default=0)
    likes_count = models.IntegerField(default=0)


class Track(models.Model):
    title = models.CharField(max_length=200, unique=True)
    playlist = models.ManyToManyField(Playlist)


class Tag(models.Model):
    title = models.CharField(max_length=100, unique=True)
    playlist = models.ManyToManyField(Playlist)
