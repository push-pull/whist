# from django.http import HttpResponse
from django.shortcuts import render

from imdb import IMDb

imdb = IMDb()

def index(request):
    return render(request, 'index.html')


def search(request):
    query = request.GET.get('query')
    if query:
        movies = imdb.search_movie(query)
    return render(
        request,
        'queryresults.html',
        {
            'query': query,
            'movies': movies,
        }
    )
