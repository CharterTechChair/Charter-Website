# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0006_auto_20151004_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='netid',
            field=models.CharField(unique=True, max_length=100, verbose_name=b'Princeton Net ID', validators=[django.core.validators.RegexValidator(b'^[0-9a-zA-Z\\.]*$', b'Only a mix of alphanumeric characters and peroids are allowed.')]),
            preserve_default=True,
        ),
    ]
