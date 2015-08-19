# coding: utf-8

from django.conf import settings
from .resource import Resource


class QuerySetRedis(object):
    # Classe criada somente para herança.
    resource = Resource()


class Tag(QuerySetRedis):

    def __init__(self, instance):
        pass


class Post(QuerySetRedis):

    def __init__(self, instance):
        pass


class Author(QuerySetRedis):

    def __init__(self, instance):
        pass
