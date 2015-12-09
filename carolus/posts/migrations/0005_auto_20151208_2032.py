# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='description_en',
            field=models.CharField(max_length=3000, null=True, verbose_name='Descripci\xf3n'),
        ),
        migrations.AddField(
            model_name='post',
            name='description_es',
            field=models.CharField(max_length=3000, null=True, verbose_name='Descripci\xf3n'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.CharField(max_length=3000, verbose_name='Descripci\xf3n'),
        ),
    ]
