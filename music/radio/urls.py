from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'search$', views.search, name='search'),

    url(r'track/create$', views.create_track, name='create_track'),
    url(r'track/delete$', views.delete_track, name='delete_track'),
    url(r'tracks/list$', views.list_tracks, name='list_tracks'),
    url(r'add_track_to_playlist$', views.add_track_to_playlist,
        name='add_track_to_playlist'),

    url(r'playlist/create$', views.create_playlist, name='create_playlist'),
    url(r'playlist/delete$', views.delete_playlist, name='delete_playlist'),
    url(r'playlist/(?P<playlist_id>[0-9]+)$', views.view_playlist,
        name='view_playlist'),
    url(r'playlists/list$', views.list_playlists, name='list_playlists'),
    url(r'increment_play_count$', views.increment_play_count,
        name='increment_play_count'),
    url(r'increment_likes_count$', views.increment_likes_count,
        name='increment_likes_count'),

    url(r'tag/create$', views.create_tag, name='create_tag'),
    url(r'tag/delete$', views.delete_tag, name='delete_tag'),
    url(r'tag/(?P<tag_id>[0-9]+)$', views.view_tag, name='view_tag'),
    url(r'tags/list$', views.list_tags, name='list_tags'),
    url(r'add_tag_to_playlist$', views.add_tag_to_playlist,
        name='add_tag_to_playlist'),
]
