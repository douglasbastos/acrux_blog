#coding: utf-8

from django.contrib import admin
from .models.models import Post, Tag

admin.site.register(Post)
admin.site.register(Tag)