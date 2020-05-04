from django.contrib import admin
from .models import Artist


# class MusicInline(admin.TabularInline):
#     model = music
#     extra = 3
#
#
# # Register your models here.
class musicAdmin(admin.ModelAdmin):
    list_display = ('track_name', 'artist', 'album')
    list_filter = ['artist', 'album']
    search_fields = ['track_name', 'artist', 'album']
#    inlines = [MusicInline]
#    fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#     ]


admin.site.register(Artist, musicAdmin)
