# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CharterClubSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('default_sophomore_meal_per_month', models.PositiveIntegerField(default=2, verbose_name=b'When a prospective is created, this is the default number of meals that will be assigned to them.')),
                ('default_member_meals_per_semester', models.PositiveIntegerField(default=4, verbose_name=b'When a member is created, this is the default number of guest meals that will be assigned to them.')),
                ('default_house_account', models.DecimalField(default=255.0, verbose_name=b'When a member is created, the default house account assigned to them', max_digits=10, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
