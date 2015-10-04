# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0005_auto_20151003_1703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prospective',
            name='events_attended',
        ),
        migrations.RemoveField(
            model_name='prospective',
            name='meals_attended',
        ),
        migrations.RemoveField(
            model_name='prospective',
            name='meals_signed_up',
        ),
    ]
