# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0007_auto_20151201_2232'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='guest_meals',
            field=models.IntegerField(default=4, verbose_name=b'number of guest meals this member has'),
            preserve_default=True,
        ),
    ]
