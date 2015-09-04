# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('meals', models.CharField(max_length=10, choices=[(b'Lunch', b'Lunch'), (b'Dinner', b'Dinner')])),
                ('allow_sophomore', models.BooleanField(default=False)),
                ('description', models.TextField(help_text=b'What are we eating today?', max_length=1000)),
                ('grill', models.CharField(help_text=b'Visible only for Lunches', max_length=1000, null=True, blank=True)),
                ('plated_option', models.CharField(help_text=b'Visible only for Dinners', max_length=1000, null=True, blank=True)),
                ('salad', models.CharField(help_text=b'For Herbivores', max_length=1000, blank=True)),
                ('special_note', models.CharField(help_text=b"i.e. 'Seniors only', or 'Meal ends early at 7:00pm'", max_length=1000, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
