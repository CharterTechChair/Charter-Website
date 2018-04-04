# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0013_auto_20171004_2104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prospectiveevententry',
            name='signup_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
