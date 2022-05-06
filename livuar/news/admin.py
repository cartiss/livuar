from django.contrib import admin

from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name')
    list_filter = ('name',)