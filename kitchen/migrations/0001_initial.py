# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.DateField()),
                ('sophomore_limit', models.IntegerField(default=0, help_text=b"Put '0' to not allow sophomores")),
                ('name', models.CharField(help_text=b'Optional Name', max_length=100, blank=True)),
                ('description', models.TextField(help_text=b'What are we eating today?', max_length=1000)),
                ('special_note', models.CharField(help_text=b"Optoinal note- i.e. 'Seniors only', or 'Meal ends early at 7:00pm'", max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lunch',
            fields=[
                ('meal_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitchen.Meal')),
                ('grill_special', models.CharField(help_text=b'Optionals', max_length=1000, blank=True)),
                ('salad', models.CharField(help_text=b'Optional', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('kitchen.meal',),
        ),
        migrations.CreateModel(
            name='Dinner',
            fields=[
                ('meal_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitchen.Meal')),
                ('plated_option', models.CharField(help_text=b'Optional', max_length=1000, blank=True)),
                ('salad', models.CharField(help_text=b'Optional', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('kitchen.meal',),
        ),
        migrations.CreateModel(
            name='Brunch',
            fields=[
                ('meal_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='kitchen.Meal')),
                ('grill_special', models.CharField(help_text=b'Optional', max_length=1000, blank=True)),
                ('omlette', models.CharField(help_text=b'Optional', max_length=1000, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('kitchen.meal',),
        ),
        migrations.AddField(
            model_name='meal',
            name='real_type',
            field=models.ForeignKey(editable=False, to='contenttypes.ContentType'),
            preserve_default=True,
        ),
    ]
