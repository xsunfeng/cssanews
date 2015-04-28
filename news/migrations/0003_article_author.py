# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20150427_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(default=datetime.datetime(2015, 4, 27, 19, 8, 48, 338007, tzinfo=utc), max_length=200),
            preserve_default=False,
        ),
    ]
