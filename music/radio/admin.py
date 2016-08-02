from django.contrib import admin

from .models import Track, Playlist, Tag


class TrackAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ('title',)

admin.site.register(Track, TrackAdmin)


class PlaylistAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ('title',)

admin.site.register(Playlist, PlaylistAdmin)


class TagAdmin(admin.ModelAdmin):
    fields = ['title']
    list_display = ('title',)

admin.site.register(Tag, TagAdmin)
