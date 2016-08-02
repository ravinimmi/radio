from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from .models import Track, Playlist, Tag


def index(request):
    return HttpResponse("Server is running.")


def search(request):
    tags = request.GET.getlist('tags')
    tag_objects = Tag.objects.filter(title__in=tags)

    playlist_objects = playlists_containing_tags(tag_objects)
    playlists = order_playlists_by_relevance(list(playlist_objects.values()))

    tags = tags_in_playlists(playlist_objects)

    response = {'playlists': playlists,
                'tags': tags
                }
    return JsonResponse(response)


def playlists_containing_tags(tag_objects):
    playlist_objects = Playlist.objects.all()
    for tag_object in tag_objects:
        playlist_objects = playlist_objects.filter(tag=tag_object)
    return playlist_objects


def tags_in_playlists(playlist_objects):
    tag_objects = Tag.objects.filter(playlist__in=playlist_objects).\
        annotate(count=Count('id')).order_by('-count').values()
    tags = list(tag_objects)
    return tags


def order_playlists_by_relevance(playlists):
    play_count_weight = 1
    likes_count_weight = 2

    def score(playlist):
        return play_count_weight * playlist['play_count']
        + likes_count_weight * playlist['likes_count']

    playlists.sort(key=score, reverse=True)
    return playlists


def increment_play_count(request):
    playlist_id = request.GET.get('playlist_id')
    try:
        playlist = Playlist.objects.get(id=playlist_id)
        playlist.play_count = playlist.play_count + 1
        playlist.save()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def increment_likes_count(request):
    playlist_id = request.GET.get('playlist_id')
    try:
        playlist = Playlist.objects.get(id=playlist_id)
        playlist.likes_count = playlist.likes_count + 1
        playlist.save()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


# Content insertion
def create_track(request):
    title = request.GET.get('title')
    try:
        track = Track(title=title)
        track.save()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def delete_track(request):
    title = request.GET.get('title')
    try:
        track = Track.objects.filter(title=title)
        track.delete()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def list_tracks(request):
    try:
        tracks = Track.objects.all().values()
        response = {'success': True, 'tracks': list(tracks)}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def create_playlist(request):
    title = request.GET.get('title')
    try:
        playlist = Playlist(title=title)
        playlist.save()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def delete_playlist(request):
    title = request.GET.get('title')
    try:
        playlist = Playlist.objects.filter(title=title)
        playlist.delete()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def list_playlists(request):
    try:
        playlists = Playlist.objects.all().values()
        response = {'success': True, 'playlists': list(playlists)}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def view_playlist(request, playlist_id):
    try:
        playlist = Playlist.objects.get(id=playlist_id)
        tracks = playlist.track_set.all().values()
        response = {'success': True,
                    'tracks': list(tracks),
                    'play_count': int(playlist.play_count),
                    'likes_count': int(playlist.likes_count)
                    }
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def add_track_to_playlist(request):
    track_id = request.GET.get('track_id')
    playlist_id = request.GET.get('playlist_id')
    try:
        track = Track.objects.get(id=track_id)
        playlist = Playlist.objects.get(id=playlist_id)
        track.playlist.add(playlist)
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def create_tag(request):
    title = request.GET.get('title')
    try:
        tag = Tag(title=title)
        tag.save()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def delete_tag(request):
    title = request.GET.get('title')
    try:
        tag = Tag.objects.filter(title=title)
        tag.delete()
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def view_tag(request, tag_id):
    try:
        tag = Tag.objects.get(id=tag_id)
        playlists = tag.playlist.all().values()
        response = {'success': True, 'playlists': list(playlists)}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def list_tags(request):
    try:
        tags = Tag.objects.all().values()
        response = {'success': True, 'tags': list(tags)}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)


def add_tag_to_playlist(request):
    tag_id = request.GET.get('tag_id')
    playlist_id = request.GET.get('playlist_id')
    try:
        tag = Tag.objects.get(id=tag_id)
        playlist = Playlist.objects.get(id=playlist_id)
        tag.playlist.add(playlist)
        response = {'success': True}
    except Exception as e:
        print("Error occured " + str(e))
        response = {'success': False}
    return JsonResponse(response)
