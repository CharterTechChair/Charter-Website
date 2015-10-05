# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0003_auto_20151004_1642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prospectivemealentry',
            options={'ordering': ['-meal']},
        ),
        migrations.AlterField(
            model_name='prospectiveevententry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 10, 5), blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 10, 5), blank=True),
            preserve_default=True,
        ),
    ]
