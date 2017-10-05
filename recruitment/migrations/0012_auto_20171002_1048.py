# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0011_auto_20161022_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospectiveevententry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2017, 10, 2), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2017, 10, 2), blank=True),
            preserve_default=True,
        ),
    ]
