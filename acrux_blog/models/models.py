# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from ..models.qs_redis import Author
from acrux_blog import qs_redis as qs

import redis
cache = redis.StrictRedis(host='127.0.0.1', port=6379, db=0)

class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Tag, self).save(*args, **kwargs)
        qs.Tag.resource.rpush('tags:all', self.name)

class Post(models.Model):
    title = models.CharField('Título', max_length=55)
    subtitled = models.CharField('Subtítulo', max_length=55)
    slug = models.SlugField(max_length=55)
    content = models.TextField('Texto')
    date_publication = models.DateTimeField(editable=False, auto_now_add=True, null=True)
    date_edition = models.DateTimeField(editable=False, auto_now=True, null=True)
    tag = models.ForeignKey(Tag)
    author = models.ForeignKey(User, verbose_name='Autor do post')

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        #is_edition deve ficar antes do super, depois o pk é criado mesmo não sendo edição
        is_edition = True if self.pk else False
        super(Post, self).save(*args, **kwargs)
        author = self.author.username.lower()
        tag = self.tag.name.lower()
        author_with_post = Author.all()
        if author not in author_with_post:
            items_author = {'first_name': self.author.first_name,'last_name': self.author.last_name}
            cache.rpush('author:all', author)
            cache.hmset('author:{}:username'.format(self.author.username), items_author)
        if not is_edition:
            cache.rpush('post:all', self.slug)
            cache.rpush('post:{}:tag'.format(tag), self.slug)
            cache.rpush('post:{}:author'.format(author), self.slug)
        items_post = {
            'title': self.title,
            'subtitled': self.subtitled,
            'slug': self.slug,
            'content': self.content, 
            'date_publication': self.date_publication,
            'date_edition': self.date_edition,
            'tag': self.tag,
            'author': self.author
            }
        cache.hmset('post:{}:slug'.format(self.slug.lower()), items_post)
