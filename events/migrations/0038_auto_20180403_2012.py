# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0037_auto_20171004_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Date of Event'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='prospective_signup_start',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateField(auto_now_add=True),
            preserve_default=True,
        ),
    ]
