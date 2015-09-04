# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospective',
            name='meals_attended',
            field=models.ManyToManyField(to='kitchen.Meal', null=True),
            preserve_default=True,
        ),
    ]
