# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import events.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0002_auto_20150910_1547'),
        ('events', '0004_auto_20150910_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ('student',)},
        ),
        migrations.RemoveField(
            model_name='entry',
            name='member',
        ),
        migrations.AddField(
            model_name='entry',
            name='student',
            field=models.ForeignKey(default='', to='charterclub.Student'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='entry',
            name='event',
            field=models.ForeignKey(related_name='entry_event_association', to='events.Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='entry',
            name='room',
            field=models.ForeignKey(related_name='entry_room_association', to='events.Room'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 0, 59, 40, 574256, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(validators=events.models.validate_image, upload_to=b'event_images/', blank=True, help_text=b'To be displayed on the website. (Optional).', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 0, 59, 40, 574256, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 0, 59, 40, 574256, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 0, 59, 40, 574256, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 0, 59, 40, 574256, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='snippet',
            field=models.TextField(help_text=b'To be displayed on the website. (Optional).', verbose_name=b'Description'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 9, 11, 0, 59, 40, 574256, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TimeField(default=datetime.time(17, 0), help_text=b'IMPORTANT. THIS IS IN MILITARY TIME.', verbose_name=b'Time of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='event',
            field=models.ForeignKey(related_name='event_room', to='events.Event'),
            preserve_default=True,
        ),
    ]
