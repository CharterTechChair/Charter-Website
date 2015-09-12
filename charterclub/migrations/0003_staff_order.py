# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0002_auto_20150910_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='order',
            field=models.IntegerField(default=1, verbose_name=b'Order of Appearance on Staff Page'),
            preserve_default=False,
        ),
    ]
