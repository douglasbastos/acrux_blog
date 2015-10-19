# coding: utf-8
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import blog

urlpatterns = [
    url(r'^index.html$', (blog.ListPosts.as_view()), name='page_index'),
    url(r'^post/author/(?P<author>[a-z0-9\-]+)/$', (blog.ListPostsAuthor.as_view()), name='author_posts'),
    url(r'^post/tag/(?P<tag>[a-z0-9\-]+)$', (blog.ListPostsTag.as_view()), name='tags_posts'),
    url(r'^post/slug/(?P<slug>[a-z0-9\-]+)/$', (blog.DetailPost.as_view()), name='post'),
]
