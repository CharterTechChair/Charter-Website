# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '__first__'),
        ('events', '0004_auto_20150510_1754'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guest', models.CharField(max_length=255, blank=True)),
                ('member', models.ForeignKey(to='charterclub.Member')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='room',
            name='guests',
        ),
        migrations.RemoveField(
            model_name='room',
            name='members',
        ),
        migrations.AddField(
            model_name='room',
            name='seatings',
            field=models.ManyToManyField(to='events.Seating'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='date_and_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='junior_signup_start',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='senior_signup_start',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='signup_end_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='event',
            name='sophomore_signup_start',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='room',
            name='name',
            field=models.CharField(max_length=255),
            preserve_default=True,
        ),
    ]
