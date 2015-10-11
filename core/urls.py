from django.conf.urls import url, patterns

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'index', name="index"),
    url(r'^search/$', 'search', name="search"),
    url(r'^movie/(?P<movie_id>[0-9]+)/$', 'movie', name="movie"),
)
