from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """An extension of Django's default user model.

    This allows for the storage of extra information about a user.
    """
    user = models.OneToOneField(User)
    movies = models.ManyToManyField('Movie', related_name='Users')


class Movie(models.Model):
    """A movie seen by a user.

    Relates to `models.UserProfile` and `models.Actor`.
    """
    name = models.CharField(max_length=255)
    imdb_id = models.IntegerField(null=False)
    actors = models.ManyToManyField('Actor', related_name='movies')


class Actor(models.Model):
    """An actor in a movie.

    Relates to `models.Movie`.
    """
    name = models.CharField(max_length=255)
    imdb_id = models.IntegerField(null=False)
