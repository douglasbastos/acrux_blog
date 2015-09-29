# coding: utf-8
from django.conf.urls import url

from .views import blog

urlpatterns = [
    # url(r'base', blog.base, name='base'),
    url(r'index.html$', blog.ListPosts.as_view(), name='page_index'),
    url(r'(?P<slug>[a-z0-9\-]+)/$', blog.DetailPost.as_view(), name='post'),
]   