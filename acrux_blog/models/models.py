# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

from acrux_blog import qs_redis as qs


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

    def _save_author(self, author):
        items_author = {'first_name': self.author.first_name,'last_name': self.author.last_name}
        qs.Author.resource.rpush('author:all', author)
        qs.Author.resource.hmset('author:{}:username'.format(self.author.username), items_author)

    def _save_post(self):
        qs.Post.resource.rpush('post:all', self.slug)
        qs.Post.resource.rpush('post:{}:tag'.format(tag), self.slug)
        qs.Post.resource.rpush('post:{}:author'.format(author), self.slug)

    @property
    def create_elements_post(self):
        items = {
            'title': self.title,
            'subtitled': self.subtitled,
            'slug': self.slug,
            'content': self.content, 
            'date_publication': self.date_publication,
            'date_edition': self.date_edition,
            'tag': self.tag,
            'author': self.author
        }
        return items

    def save(self, *args, **kwargs):
        #se tiver pk é uma edição
        is_editing = True if self.pk else False
        super(Post, self).save(*args, **kwargs)
        tag = self.tag.name.lower()
        author = self.author.username.lower()
        import ipdb; ipdb.set_trace()
        author_with_post = qs.Author.resource.all()
        if author not in author_with_post:
            self._save_author(author)
        if not is_editing:
            self._save_post()
        items_post = create_elements_post
        qs.Post.resource.hmset('post:{}:slug'.format(self.slug.lower(), items_post))
