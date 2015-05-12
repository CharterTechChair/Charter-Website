# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150512_0410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='snippet',
            field=models.CharField(max_length=10000, verbose_name=b'Description', blank=True),
            preserve_default=True,
        ),
    ]
