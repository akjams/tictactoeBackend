from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.games_root),
    url(r'^(?P<gameid>[0-9]+)$', views.games_gameid)
]