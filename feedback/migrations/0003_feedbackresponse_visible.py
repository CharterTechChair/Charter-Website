# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_feedbackresponse_display_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedbackresponse',
            name='visible',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
    ]
