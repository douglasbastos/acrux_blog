# coding: utf-8

import redis
cache = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

class Post:

    @classmethod
    def all(cls):
        return cache.lrange('post:all', 0, -1)

    @classmethod
    def by_slug(cls, slug):
        keys = ['title', 'slug', 'content', 'author', 'date_publication', 'date_edition', 'tag']
        for name in keys:
            post[name] = cache.hget('post:{}:slug'.format(slug), name)
        return post

    @classmethod
    def relacionados_by_tag(cls, tag):
        return cache.lrange('post:{}:tag'.format(tag), 0, -1)

    @classmethod
    def relacionados_by_author(cls, author):
        return cache.lrange('post:{}:author'.format(author), 0, -1)

    @classmethod
    def title(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'title')[0]

    @classmethod
    def subtitled(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'subtitled')[0]

    @classmethod
    def content(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'content')[0]

    @classmethod 
    def date_publication(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'date_publication')[0]

    @classmethod
    def date_edition(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'date_edition')[0]

    @classmethod
    def tag(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'tag')[0]

    @classmethod
    def author(cls, slug):
        return cache.hmget('post:{}:slug'.format(slug), 'author')[0]


class Author:

    @classmethod
    def last_name(cls, author):
        return cache.hmget('author:{}:username'.format(author), 'last_name')[0]

    @classmethod
    def first_name(cls, author):
        return cache.hmget('author:{}:username'.format(author), 'first_name')[0]
    