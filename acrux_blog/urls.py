# coding: utf-8
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from .views import blog

urlpatterns = [
    # url(r'base', blog.base, name='base'),
    url(r'index.html$', cache_page(60 * 15)(blog.ListPosts.as_view()), name='page_index'),
    url(r'(?P<slug>[a-z0-9\-]+)/$', cache_page(60 * 15)(blog.DetailPost.as_view()), name='post'),
]   