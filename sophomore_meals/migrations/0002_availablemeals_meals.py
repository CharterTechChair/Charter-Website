# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sophomore_meals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='availablemeals',
            name='meals',
            field=models.CharField(default=datetime.datetime(2015, 9, 3, 18, 39, 1, 583959, tzinfo=utc), max_length=1, choices=[(b'L', b'Lunch'), (b'D', b'Dinner')]),
            preserve_default=False,
        ),
    ]
