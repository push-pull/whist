from django.conf.urls import url, patterns

# from core import views

urlpatterns = patterns(
    'core.views',
    url(r'^$', 'index', name="index"),
    url(r'^search/$', 'search', name="search"),
)
