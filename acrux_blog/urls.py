#coding: utf-8
from django.conf.urls import url

from .views import blog, blog_redis

urlpatterns = [
    # url(r'base', blog.base, name='base'),
    url(r'index.html', blog.ListPosts.as_view(), name='page_index'),
    url(r'blog/(?P<slug>[a-z0-9\-]+)/$', blog.DetailPost.as_view(), name='post'),

    #redis
    url(r'redis.html', blog_redis.ListPosts.as_view(), name='page_index_with_redis'),
    url(r'redis/(?P<slug>[a-z0-9\-]+)/$', blog_redis.DetailPost.as_view(), name='posts_with_redis'),
]   