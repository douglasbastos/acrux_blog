# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=55, verbose_name=b'T\xc3\xadtulo')),
                ('subtitled', models.CharField(max_length=55, verbose_name=b'Subt\xc3\xadtulo')),
                ('slug', models.SlugField(max_length=55)),
                ('content', models.TextField(verbose_name=b'Texto')),
                ('author', models.ForeignKey(verbose_name=b'Autor do post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=55)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(to='simple_blog.Tag'),
        ),
    ]
