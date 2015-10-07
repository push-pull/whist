#!/usr/bin/env python

"""
Provides a collection of useful functions to reduce the time spent writing 
boilerplate code.
"""

import imdb 
db = imdb.IMDb()

def get_character(person, movie_id):
	"""Retrieves a Character object.

	Args:
		person: The person who plays the character.
		movie_id: The ID of the movie or TV show.

	Returns:
		A character object.
	"""
	movie = db.get_movie(movie_id)
	cast = movie['cast']

	for actor in cast:
		if actor.isSamePerson(person):
			return actor.currentRole
	else:
		return None