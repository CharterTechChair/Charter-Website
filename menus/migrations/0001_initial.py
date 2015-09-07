# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('lunch_food', models.TextField()),
                ('dinner_food', models.TextField()),
            ],
            options={
                'ordering': ['date'],
            },
            bases=(models.Model,),
        ),
    ]
