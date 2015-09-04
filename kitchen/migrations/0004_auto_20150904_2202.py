# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_auto_20150904_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='grill',
            field=models.CharField(default='', help_text=b'Visible only for Lunches', max_length=1000, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='name',
            field=models.CharField(default='', help_text=b'Optional Name', max_length=100, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='plated_option',
            field=models.CharField(default='', help_text=b'Visible only for Dinners', max_length=1000, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='special_note',
            field=models.CharField(default='', help_text=b"i.e. 'Seniors only', or 'Meal ends early at 7:00pm'", max_length=1000, blank=True),
            preserve_default=False,
        ),
    ]
