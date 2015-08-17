# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simple_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_edition',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='date_publication',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
