# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sophomore_meals', '0003_auto_20150903_1843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('meals', models.CharField(max_length=1, choices=[(b'Lunch', b'Lunch'), (b'Dinner', b'Dinner')])),
                ('allow_sophomore', models.BooleanField(default=True)),
                ('description_s', models.CharField(max_length=1000)),
                ('special_note', models.CharField(max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.DeleteModel(
            name='AvailableMeals',
        ),
    ]
