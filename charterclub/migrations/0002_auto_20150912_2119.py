# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0001_initial'),
        ('kitchen', '0001_initial'),
        ('contenttypes', '0001_initial'),
    ]

    operations = [
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
        migrations.AddField(
            model_name='person',
            name='real_type',
            field=models.ForeignKey(editable=False, to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]
