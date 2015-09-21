# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150920_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='display_to_non_members',
            field=models.BooleanField(default=True, help_text=b'Are non-members allowed to see this event?', verbose_name=b'Public Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 3, 20, 8, 248616, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 3, 20, 8, 248616, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_limit',
            field=models.IntegerField(default=0, help_text=b'set 0 to not allow prospectives. This will also hide it on the website from them (email me, Quan, to turn this feature off).', verbose_name=b'Prospectives Limit'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 3, 20, 8, 248616, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 3, 20, 8, 248616, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 3, 20, 8, 248616, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 21, 3, 20, 8, 248616, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
