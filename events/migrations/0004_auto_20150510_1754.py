# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_delete_socialevent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='end_time',
            new_name='signup_end_time',
        ),
        migrations.AlterField(
            model_name='event',
            name='snippet',
            field=models.CharField(max_length=10000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
