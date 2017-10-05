# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import charterclub.models


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0009_auto_20161001_2147'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='image',
            field=models.ImageField(validators=[charterclub.models.validate_image], upload_to=b'member_images/', blank=True, help_text=b'(optional)', null=True),
            preserve_default=True,
        ),
    ]
