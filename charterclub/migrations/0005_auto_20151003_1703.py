# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
        ('charterclub', '0004_auto_20151003_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='prospective',
            name='events_attended',
            field=models.IntegerField(default=0, verbose_name=b'Number of events attended'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prospective',
            name='meals_attended',
            field=models.ManyToManyField(related_name='meals_attended', to='kitchen.Meal', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prospective',
            name='meals_signed_up',
            field=models.ManyToManyField(related_name='meals_signed_up', to='kitchen.Meal', blank=True),
            preserve_default=True,
        ),
    ]
