from django.contrib import admin
from .models import Photo, Theme, Author, Style

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'time', 'theme')

class ThemeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'style')

admin.site.register(Style)
admin.site.register(Theme,ThemeAdmin)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Author)





















