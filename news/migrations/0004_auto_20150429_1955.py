# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='desc',
            field=models.CharField(default=0, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='thumb_url',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
