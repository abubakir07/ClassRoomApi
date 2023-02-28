from django.contrib import admin

from apps.themes.models import Theme

@admin.register(Theme)
class ThemeAdmin(admin.ModelAdmin):
    list_display = ['title', 'course']
    