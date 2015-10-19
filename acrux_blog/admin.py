# coding: utf-8

from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitled', 'slug',
                    'date_publication', 'date_edition',
                    'tag', 'author')
    search_fields = ['title']

    fieldsets = ((None, {
        'fields': ('title', 'subtitled', 'content', 'tag', 'author'),
    }),)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
