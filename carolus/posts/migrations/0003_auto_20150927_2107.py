# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150927_2035'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['creation_date'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='post',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 27, 21, 7, 57, 877227, tzinfo=utc), verbose_name='Fecha de creaci\xf3n', auto_now_add=True),
            preserve_default=False,
        ),
    ]
