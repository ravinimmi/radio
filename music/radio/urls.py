from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'search$', views.search, name='search'),

    url(r'create_track$', views.create_track, name='create_track'),
    url(r'delete_track$', views.delete_track, name='delete_track'),
    url(r'list_tracks$', views.list_tracks, name='list_tracks'),
    url(r'add_track_to_playlist$', views.add_track_to_playlist,
        name='add_track_to_playlist'),

    url(r'create_playlist$', views.create_playlist, name='create_playlist'),
    url(r'delete_playlist$', views.delete_playlist, name='delete_playlist'),
    url(r'view_playlist$', views.view_playlist, name='view_playlist'),
    url(r'list_playlists$', views.list_playlists, name='list_playlists'),
    url(r'increment_play_count$', views.increment_play_count,
        name='increment_play_count'),
    url(r'increment_likes_count$', views.increment_likes_count,
        name='increment_likes_count'),

    url(r'create_tag$', views.create_tag, name='create_tag'),
    url(r'delete_tag$', views.delete_tag, name='delete_tag'),
    url(r'view_tag$', views.view_tag, name='view_tag'),
    url(r'list_tags$', views.list_tags, name='list_tags'),
    url(r'add_tag_to_playlist$', views.add_tag_to_playlist,
        name='add_tag_to_playlist'),
]
