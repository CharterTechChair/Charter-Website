# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0005_auto_20151012_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospectiveevententry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 12, 2), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='points',
            field=models.DecimalField(default=1, verbose_name=b'Number of points this meal is worth', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 12, 2), blank=True),
            preserve_default=True,
        ),
    ]
