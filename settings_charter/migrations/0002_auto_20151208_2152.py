# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings_charter', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='charterclubsettings',
            name='default_house_account',
        ),
        migrations.AddField(
            model_name='charterclubsettings',
            name='default_house_account_for_new_account',
            field=models.DecimalField(default=255.0, max_digits=10, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='charterclubsettings',
            name='default_member_meals_per_semester',
            field=models.PositiveIntegerField(default=4),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='charterclubsettings',
            name='default_sophomore_meal_per_month',
            field=models.PositiveIntegerField(default=2),
            preserve_default=True,
        ),
    ]
