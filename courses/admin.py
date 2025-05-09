# admin.py
from django.contrib import admin
from .models import Course, Episode

class EpisodeInline(admin.TabularInline):
    model = Episode
    extra = 1  # Adds an empty form for adding an episode

class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode_count', 'date_added')
    search_fields = ('title',)
    inlines = [EpisodeInline]

admin.site.register(Course, CourseAdmin)
admin.site.register(Episode)
