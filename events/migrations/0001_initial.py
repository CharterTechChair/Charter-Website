# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('snippet', models.CharField(max_length=150, blank=True)),
                ('date_and_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('sophomore_signup_start', models.DateTimeField(blank=True)),
                ('junior_signup_start', models.DateTimeField(blank=True)),
                ('senior_signup_start', models.DateTimeField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.CharField(max_length=10, choices=[(b'Monday', b'Monday'), (b'Tuesday', b'Tuesday'), (b'Wednesday', b'Wednesday'), (b'Thursday', b'Thursday'), (b'Friday', b'Friday'), (b'Saturday', b'Saturday'), (b'Sunday', b'Sunday')])),
                ('lunch_food', models.CharField(max_length=1000)),
                ('dinner_food', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=40)),
                ('max_capacity', models.IntegerField(verbose_name=b'Max capacity for that room for a specific event')),
                ('guests', models.ManyToManyField(to='charterclub.Guest')),
                ('members', models.ManyToManyField(to='charterclub.Member')),
            ],
            options={
                'ordering': ('name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocialEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('snippet', models.CharField(max_length=150, blank=True)),
                ('date_and_time', models.DateTimeField(blank=True)),
                ('end_time', models.DateTimeField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='event',
            name='rooms',
            field=models.ManyToManyField(to='events.Room'),
            preserve_default=True,
        ),
    ]
