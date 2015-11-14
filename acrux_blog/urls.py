# coding: utf-8
from django.conf.urls import url
from django.conf import settings
from django.views.decorators.cache import cache_page

from . import views

urlpatterns = [
    # without cache
    url(r'^$', views.ListPosts.as_view(), name='page_index'),
    url(r'^post/author/(?P<author>[a-zA-Z0-9\-]+)/$', views.ListPostsAuthor.as_view(), name='author_posts'),
    url(r'^post/tag/(?P<tag>[a-z0-9\-]+)$', views.ListPostsTag.as_view(), name='tags_posts'),
    url(r'^post/slug/(?P<slug>[a-z0-9\-]+)/$', views.DetailPost.as_view(), name='post'),

    # with cache
    url(r'^cache/', cache_page(settings.TIME_CACHE)(views.ListPosts.as_view()), name='page_index_cache'),
    url(r'^post_cache/author/(?P<author>[a-zA-Z0-9\-]+)/$', cache_page(settings.TIME_CACHE)(views.ListPostsAuthor.as_view()), name='author_posts_cache'),
    url(r'^post_cache/tag/(?P<tag>[a-z0-9\-]+)$', cache_page(settings.TIME_CACHE)(views.ListPostsTag.as_view()), name='tags_posts_cache'),
    url(r'^post_cache/slug/(?P<slug>[a-z0-9\-]+)/$', cache_page(settings.TIME_CACHE)(views.DetailPost.as_view()), name='post_cache'),
]
