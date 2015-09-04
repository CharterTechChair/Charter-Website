# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='name',
            field=models.CharField(help_text=b'Optional Name', max_length=10, null=True, blank=True),
            preserve_default=True,
        ),
    ]
