# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='day',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='date',
            field=models.DateField(default=datetime.date(2015, 5, 10)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='dinner_food',
            field=models.TextField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='lunch_food',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
