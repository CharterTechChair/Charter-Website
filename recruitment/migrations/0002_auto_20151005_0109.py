# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prospectivemealentry',
            options={'ordering': ['-meal']},
        ),
        migrations.AddField(
            model_name='prospectivemealentry',
            name='has_been_checked',
            field=models.BooleanField(default=False, verbose_name=b'Has an officer checked this meal or not?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prospectivemealentry',
            name='points',
            field=models.DecimalField(default=1, verbose_name=b'Number of points this event is worth', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=b'Has this person completed the meal?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 10, 5), blank=True),
            preserve_default=True,
        ),
    ]
