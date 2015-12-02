# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import events.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_auto_20151201_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='downloadable_file',
            field=models.FileField(validators=[events.models.validate_file], upload_to=b'event_files/', blank=True, help_text=b"For example, the winter formals menu or any other resource you'd like to share.                                                     If you want to share multiple files, upload the .zip (Optional).", null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 20, 13, 712187, tzinfo=utc), verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 20, 13, 712187, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 20, 13, 712187, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 20, 13, 712187, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 20, 13, 712187, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(default=datetime.datetime(2015, 12, 2, 4, 20, 13, 712187, tzinfo=utc), blank=True),
            preserve_default=True,
        ),
    ]
