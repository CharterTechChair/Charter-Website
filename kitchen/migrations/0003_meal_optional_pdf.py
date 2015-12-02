# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import kitchen.models


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0002_auto_20151011_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='optional_pdf',
            field=models.FileField(blank=True, null=True, upload_to=b'meal_optional_pdf/', validators=[kitchen.models.validate_file]),
            preserve_default=True,
        ),
    ]
