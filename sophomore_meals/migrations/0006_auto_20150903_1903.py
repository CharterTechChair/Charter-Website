# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sophomore_meals', '0005_auto_20150903_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='description_s',
        ),
        migrations.AddField(
            model_name='meal',
            name='course',
            field=models.CharField(default=datetime.datetime(2015, 9, 3, 19, 3, 32, 822222, tzinfo=utc), help_text=b'What are we eating today?', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='grill',
            field=models.CharField(max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meal',
            name='salad',
            field=models.CharField(default=datetime.datetime(2015, 9, 3, 19, 3, 38, 454009, tzinfo=utc), max_length=1000, blank=True),
            preserve_default=False,
        ),
    ]
