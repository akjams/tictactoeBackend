from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^games/games/$', views.games_root),
    url(r'^games/(?P<gameid>[0-9]+)$', views.games_gameid),
    url(r'^users/$', views.users_root)
]