# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sophomore_meals', '0002_availablemeals_meals'),
    ]

    operations = [
        migrations.AlterField(
            model_name='availablemeals',
            name='meals',
            field=models.CharField(max_length=1, choices=[(b'Lunch', b'Lunch'), (b'Lunch', b'Dinner')]),
            preserve_default=True,
        ),
    ]
