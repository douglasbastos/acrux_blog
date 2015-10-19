# coding: utf-8

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __unicode__(self):
        return self.name


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
