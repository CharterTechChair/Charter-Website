# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0002_auto_20150919_2154'),
        ('events', '0003_auto_20150920_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(default='', to='charterclub.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 20, 56, 42, 57082, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 20, 56, 42, 57082, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 20, 56, 42, 57082, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 20, 56, 42, 57082, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 20, 56, 42, 57082, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 20, 20, 56, 42, 57082, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
