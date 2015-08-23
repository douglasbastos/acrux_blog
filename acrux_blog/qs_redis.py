# coding: utf-8

from django.conf import settings
from .resource import Resource


class QuerySetRedis(object):
    # Classe criada somente para herança.
    resource = Resource()

    def all(self):
        import ipdb; ipdb.set_trace()

class Tag(QuerySetRedis):

    def __init__(self):
        pass


class Post(QuerySetRedis):

    def __init__(self):
        pass

    @classmethod
    def all(cls):
        return cls.resource.lrange('post:all', 0, -1)

    @classmethod
    def by_slug(cls, slug):
        keys = ['title', 'slug', 'content', 'author', 'date_publication', 'date_edition', 'tag']
        for name in keys:
            post[name] = cls.resource.hget('post:{}:slug'.format(slug), name)
        return post

    @classmethod
    def relacionados_by_tag(cls, tag):
        return cls.resource.lrange('post:{}:tag'.format(tag), 0, -1)

    @classmethod
    def relacionados_by_author(cls, author):
        return cls.resource.lrange('post:{}:author'.format(author), 0, -1)

    @classmethod
    def title(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'title')[0]

    @classmethod
    def subtitled(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'subtitled')[0]

    @classmethod
    def content(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'content')[0]

    @classmethod 
    def date_publication(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'date_publication')[0]

    @classmethod
    def date_edition(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'date_edition')[0]

    @classmethod
    def tag(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'tag')[0]

    @classmethod
    def author(cls, slug):
        return cls.resource.hmget('post:{}:slug'.format(slug), 'author')[0]



class Author(QuerySetRedis):

    def __init__(self):
        pass

    @classmethod
    def all(cls):
        return cls.resource.lrange('author:all', 0, -1)

    @classmethod
    def last_name(cls, author):
        return cls.resource.hmget('author:{}:username'.format(author), 'last_name')[0]

    @classmethod
    def first_name(cls, author):
        return cls.resource.hmget('author:{}:username'.format(author), 'first_name')[0]
