# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import events.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20151201_2320'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='downloadable_file_label',
            field=models.CharField(help_text=b'To tell people on the website what your downloadble file means.', max_length=255, null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 30, 21, 540993, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='downloadable_file',
            field=models.FileField(validators=[events.models.validate_file], upload_to=b'event_files/', blank=True, help_text=b"For example, this could be winter formals menu or any other resource you'd like to share.                                                        If you want to share multiple files, be a man, zip the folder and upload the .zip (Optional).", null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 30, 21, 540993, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 30, 21, 540993, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 30, 21, 540993, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 30, 21, 540993, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 30, 21, 540993, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
