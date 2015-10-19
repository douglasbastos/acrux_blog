# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('acrux_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=datetime.date(2015, 10, 19), verbose_name=b'Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='date_edition',
            field=models.DateTimeField(auto_now=True, verbose_name=b'\xc3\x9altima altera\xc3\xa7\xc3\xa3o', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='date_publication',
            field=models.DateTimeField(auto_now_add=True, verbose_name=b'Criado em', null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name=b'SlugSlug'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(unique=True, max_length=55, verbose_name=b'T\xc3\xadtulo'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True, max_length=55),
        ),
    ]
