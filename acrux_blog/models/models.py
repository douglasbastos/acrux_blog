# coding: utf-8
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Tag(models.Model):
    name = models.CharField(max_length=55)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    title = models.CharField('Título', max_length=55, unique=True)
    subtitled = models.CharField('Subtítulo', max_length=55)
    slug = models.SlugField(unique=True)
    content = models.TextField('Texto')
    date_publication = models.DateTimeField('Criado em', editable=False, auto_now_add=True, null=True)
    date_edition = models.DateTimeField('Última alteração', editable=False, auto_now=True, null=True)
    tag = models.ForeignKey(Tag)
    author = models.ForeignKey(User, verbose_name='Autor do post')

    class Meta:
        verbose_name = u'Post'
        verbose_name_plural = u'Posts'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
