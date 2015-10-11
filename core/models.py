from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    An extension of Django's default user model.

    This allows for the storage of extra information about a user.
    """
    movies = models.ManyToManyField('Movie', related_name='Users')
    user = models.OneToOneField(User)


class Movie(models.Model):
    """
    A movie seen by a user.

    Relates to `models.UserProfile` and `models.Actor`.
    """
    actors = models.ManyToManyField('Actor', related_name='movies')
    imdb_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)

    def __str__(self):
        """String representation of a Movie"""
        return "%d - \"%s\"" % (self.imdb_id, self.title)

    def common_actors(self, movie_id):
        """
        Find actors who appear in both `self` and `movie`

        Args:
            self: The movie itself.
            movie_id: The IMDb ID of the movie to compare with.

        Returns:
            A set of Actor objects.
        """

        self_actors_set = set(self.actors.all())

        try:
            other_movie = Movie.objects.get(imdb_id=movie_id)
        except:
            return None
        other_actors_set = set(other_movie.actors.all())

        return self_actors_set.intersection(other_actors_set)


class Actor(models.Model):
    """
    An actor in a movie.

    Relates to `models.Movie`.
    """
    imdb_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        """String representation of an Actor"""
        return "%d - %s" % (self.imdb_id, self.name)
