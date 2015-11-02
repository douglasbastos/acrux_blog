# coding: utf-8
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    url(r'^$', (views.ListPosts.as_view()), name='page_index'),
    url(r'^post/author/(?P<author>[a-zA-Z0-9\-]+)/$', (views.ListPostsAuthor.as_view()), name='author_posts'),
    url(r'^post/tag/(?P<tag>[a-z0-9\-]+)$', (views.ListPostsTag.as_view()), name='tags_posts'),
    url(r'^post/slug/(?P<slug>[a-z0-9\-]+)/$', (views.DetailPost.as_view()), name='post'),
]
