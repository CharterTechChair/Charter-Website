# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0002_auto_20150922_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospective',
            name='events_attended',
            field=models.IntegerField(default=0, verbose_name=b'Number of events attended'),
            preserve_default=True,
        ),
    ]
