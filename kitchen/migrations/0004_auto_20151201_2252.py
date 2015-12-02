# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0003_meal_optional_pdf'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='brunch',
            name='grill_special',
        ),
        migrations.RemoveField(
            model_name='brunch',
            name='omlette',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='plated_option',
        ),
        migrations.RemoveField(
            model_name='dinner',
            name='salad',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='grill_special',
        ),
        migrations.RemoveField(
            model_name='lunch',
            name='salad',
        ),
    ]
