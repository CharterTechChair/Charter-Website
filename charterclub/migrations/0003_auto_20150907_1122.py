# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0002_auto_20150907_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='officer',
            name='order',
            field=models.IntegerField(default=1, max_length=100, verbose_name=b'Apperance Order (on Officer Page)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='netid',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'Princeton Net ID', validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z]*$', b'Only alphanumeric characters are allowed.')]),
            preserve_default=True,
        ),
    ]
