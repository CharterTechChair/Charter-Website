# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kitchen', '0001_initial'),
        ('charterclub', '0004_auto_20151003_1641'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProspectiveMealEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('completed', models.BooleanField(default=False, verbose_name=b'Has this person completed the meal')),
                ('signup_date', models.DateField(blank=True)),
                ('meal', models.ForeignKey(to='kitchen.Meal')),
                ('prospective', models.ForeignKey(to='charterclub.Prospective')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
