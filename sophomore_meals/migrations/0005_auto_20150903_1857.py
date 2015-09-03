# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sophomore_meals', '0004_auto_20150903_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meals',
            field=models.CharField(max_length=10, choices=[(b'Lunch', b'Lunch'), (b'Dinner', b'Dinner')]),
            preserve_default=True,
        ),
    ]
