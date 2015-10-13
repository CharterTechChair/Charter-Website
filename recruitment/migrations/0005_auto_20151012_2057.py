# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0004_auto_20151011_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospectiveevententry',
            name='has_been_checked',
        ),
        migrations.RemoveField(
            model_name='prospectivemealentry',
            name='has_been_checked',
        ),
        migrations.AlterField(
            model_name='prospectiveevententry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 10, 13), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 10, 13), blank=True),
            preserve_default=True,
        ),
    ]
