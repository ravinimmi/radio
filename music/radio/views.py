from django.http import HttpResponse, JsonResponse
from django.db.models import Count
from django.db import IntegrityError
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
    tag_objects = Tag.objects.filter(playlists__in=playlist_objects).\
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
    playlist_id = request.POST.get('playlist_id')
    try:
        playlist = Playlist.objects.get(id=playlist_id)
        playlist.play_count = playlist.play_count + 1
        playlist.save()
        response = JsonResponse({'success': True})
    except Playlist.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Playlist does not exist."},
                                status=404)
    return response


def increment_likes_count(request):
    playlist_id = request.POST.get('playlist_id')
    try:
        playlist = Playlist.objects.get(id=playlist_id)
        playlist.likes_count = playlist.likes_count + 1
        playlist.save()
        response = JsonResponse({'success': True})
    except Playlist.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Playlist does not exist."},
                                status=404)
    return response


# Content insertion
def create_track(request):
    title = request.POST.get('title')
    try:
        Track(title=title).save()
        response = JsonResponse({'success': True})
    except IntegrityError:
        response = JsonResponse({'success': False,
                                 'error': "Track already exists exist."},
                                status=409)
    return response


def delete_track(request):
    title = request.POST.get('title')
    try:
        Track.objects.get(title=title).delete()
        response = JsonResponse({'success': True})
    except Track.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Track does not exist."}, status=404)
    return response


def list_tracks(request):
    tracks = Track.objects.all().values()
    response = {'success': True, 'tracks': list(tracks)}
    return JsonResponse(response)


def create_playlist(request):
    title = request.POST.get('title')
    try:
        Playlist(title=title).save()
        response = JsonResponse({'success': True})
    except IntegrityError:
        response = JsonResponse({'success': False,
                                 'error': "Playlist already exists exist."},
                                status=409)
    return response


def delete_playlist(request):
    title = request.POST.get('title')
    try:
        Playlist.objects.get(title=title).delete()
        response = JsonResponse({'success': True})
    except Playlist.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Playlist does not exist."},
                                status=404)
    return response


def list_playlists(request):
    playlists = Playlist.objects.all().values()
    response = {'success': True, 'playlists': list(playlists)}
    return JsonResponse(response)


def view_playlist(request, playlist_id):
    try:
        playlist = Playlist.objects.get(id=playlist_id)
        tracks = playlist.track_set.all().values()
        response = JsonResponse({'success': True,
                                 'tracks': list(tracks),
                                 'play_count': playlist.play_count,
                                 'likes_count': playlist.likes_count
                                 })
    except Playlist.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Playlist does not exist."},
                                status=404)
    return response


def add_track_to_playlist(request):
    track_id = request.POST.get('track_id')
    playlist_id = request.POST.get('playlist_id')
    try:
        track = Track.objects.get(id=track_id)
        playlist = Playlist.objects.get(id=playlist_id)
        track.playlists.add(playlist)
        response = JsonResponse({'success': True})
    except Track.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Track does not exist."},
                                status=404)
    except Playlist.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Playlist does not exist."},
                                status=404)
    return response


def create_tag(request):
    title = request.POST.get('title')
    try:
        Tag(title=title).save()
        response = JsonResponse({'success': True})
    except IntegrityError:
        response = JsonResponse({'success': False,
                                 'error': "Tag already exists exist."},
                                status=409)
    return response


def delete_tag(request):
    title = request.POST.get('title')
    try:
        Tag.objects.get(title=title).delete()
        response = JsonResponse({'success': True})
    except Tag.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Tag does not exist."}, status=404)
    return response


def view_tag(request, tag_id):
    try:
        tag = Tag.objects.get(id=tag_id)
        playlists = tag.playlists.all().values()
        response = JsonResponse({'success': True,
                                 'playlists': list(playlists)})
    except Tag.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Tag does not exist."}, status=404)
    return response


def list_tags(request):
    tags = Tag.objects.all().values()
    response = {'success': True, 'tags': list(tags)}
    return JsonResponse(response)


def add_tag_to_playlist(request):
    tag_id = request.POST.get('tag_id')
    playlist_id = request.POST.get('playlist_id')
    try:
        tag = Tag.objects.get(id=tag_id)
        playlist = Playlist.objects.get(id=playlist_id)
        tag.playlists.add(playlist)
        response = JsonResponse({'success': True})
    except Tag.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Tag does not exist."},
                                status=404)
    except Playlist.DoesNotExist:
        response = JsonResponse({'success': False,
                                 'error': "Playlist does not exist."},
                                status=404)
    return response
