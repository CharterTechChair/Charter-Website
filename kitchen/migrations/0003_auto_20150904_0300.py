# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_meal_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='meal',
            name='allow_sophomore',
        ),
        migrations.AddField(
            model_name='meal',
            name='sophomore_limit',
            field=models.IntegerField(default=0, help_text=b"Put '0' to not allow sophomores"),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(help_text=b'Optional Name', max_length=100, null=True, blank=True),
            preserve_default=True,
        ),
    ]
