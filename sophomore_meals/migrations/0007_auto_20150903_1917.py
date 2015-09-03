# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sophomore_meals', '0006_auto_20150903_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='course',
        ),
        migrations.AddField(
            model_name='meal',
            name='description',
            field=models.TextField(default=datetime.datetime(2015, 9, 3, 19, 17, 23, 698281, tzinfo=utc), help_text=b'What are we eating today?', max_length=1000),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='meal',
            name='plated_option',
            field=models.CharField(help_text=b'Only for Dinners', max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='allow_sophomore',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='grill',
            field=models.CharField(help_text=b'Only for Lunches', max_length=1000, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='salad',
            field=models.CharField(help_text=b'For both', max_length=1000, blank=True),
            preserve_default=True,
        ),
    ]
