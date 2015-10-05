# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20151004_2348'),
        ('recruitment', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProspectiveEventEntry',
            fields=[
                ('entry_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Entry')),
                ('has_been_checked', models.BooleanField(default=False, verbose_name=b'Has an officer checked this prospective into this event?')),
                ('signup_date', models.DateField(default=datetime.date(2015, 10, 5), blank=True)),
                ('points', models.DecimalField(default=1, verbose_name=b'Number of points this event is worth', max_digits=5, decimal_places=2)),
                ('completed', models.BooleanField(default=False, verbose_name=b'Has this person completed the meal')),
            ],
            options={
            },
            bases=('events.entry',),
        ),
        migrations.AddField(
            model_name='prospectivemealentry',
            name='has_been_checked',
            field=models.BooleanField(default=False, verbose_name=b'Has an officer checked this meal or not?'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='prospectivemealentry',
            name='points',
            field=models.DecimalField(default=1, verbose_name=b'Number of points this event is worth', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='completed',
            field=models.BooleanField(default=False, verbose_name=b'Has this person completed the meal?'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='prospectivemealentry',
            name='signup_date',
            field=models.DateField(default=datetime.date(2015, 10, 5), blank=True),
            preserve_default=True,
        ),
    ]
