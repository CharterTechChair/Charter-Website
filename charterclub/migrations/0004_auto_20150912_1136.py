# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0003_staff_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officer',
            name='order',
            field=models.IntegerField(verbose_name=b'Order of Appearance on Officer Page', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='staff',
            name='order',
            field=models.IntegerField(verbose_name=b'Order of Appearance on Staff Page', blank=True),
            preserve_default=True,
        ),
    ]
