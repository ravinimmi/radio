from django.http import HttpResponse, JsonResponse
from .models import Track, Playlist, Tag


def index(request):
    return HttpResponse("Server is running.")

# todo
def search(request):
    tags = request.GET.getlist('tags')
    response = {}
    return JsonResponse(response)


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


# Content creation
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


def view_playlist(request):
    playlist_id = request.GET.get('playlist_id')
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


def view_tag(request):
    tag_id = request.GET.get('tag_id')
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
