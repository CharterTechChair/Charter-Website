# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import events.models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('charterclub', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer_text', models.CharField(max_length=1000.0, verbose_name=b'Answer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('guest', models.CharField(max_length=1000, blank=True)),
                ('answers', models.ManyToManyField(to='events.Answer')),
            ],
            options={
                'ordering': ('event', 'room', 'student'),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(help_text=b'Name of the Event', max_length=255, verbose_name=b'Title')),
                ('snippet', models.TextField(help_text=b'To be displayed on the website. (Optional).', verbose_name=b'Description')),
                ('image', models.ImageField(validators=[events.models.validate_image], upload_to=b'event_images/', blank=True, help_text=b'To be displayed on the website. (Optional).', null=True)),
                ('is_points_event', models.BooleanField(default=False, help_text=b'Do Prospectives who attend get points?', verbose_name=b'Is Point Event:')),
                ('prospective_limit', models.IntegerField(default=0, help_text=b'set 0 to not allow prospectives', verbose_name=b'Prospectives Limit')),
                ('guest_limit', models.IntegerField(default=1, help_text=b'0 = No guests allowed. -1 = As many guests as they can.', verbose_name=b'Guest Limit')),
                ('date', models.DateField(default=datetime.datetime(2015, 9, 20, 1, 54, 2, 318632, tzinfo=utc), verbose_name=b'Date of Event')),
                ('time', models.TimeField(default=datetime.time(17, 0), help_text=b'IMPORTANT. THIS IS IN MILITARY TIME.', verbose_name=b'Time of Event')),
                ('signup_end_time', models.DateField(default=datetime.datetime(2015, 9, 20, 1, 54, 2, 318632, tzinfo=utc))),
                ('prospective_signup_start', models.DateField(default=datetime.datetime(2015, 9, 20, 1, 54, 2, 318632, tzinfo=utc), blank=True)),
                ('sophomore_signup_start', models.DateField(default=datetime.datetime(2015, 9, 20, 1, 54, 2, 318632, tzinfo=utc), blank=True)),
                ('junior_signup_start', models.DateField(default=datetime.datetime(2015, 9, 20, 1, 54, 2, 318632, tzinfo=utc), blank=True)),
                ('senior_signup_start', models.DateField(default=datetime.datetime(2015, 9, 20, 1, 54, 2, 318632, tzinfo=utc), blank=True)),
                ('signup_time', models.TimeField(default=datetime.time(17, 0), help_text=b'IMPORTANT. THIS IS IN MILITARY TIME.', verbose_name=b'Start/End  Time for signups')),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_text', models.CharField(max_length=1000.0, verbose_name=b'Question Text')),
                ('help_text', models.CharField(max_length=1000.0, verbose_name=b'Help Text')),
                ('event', models.ForeignKey(to='events.Event')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(help_text=b'Where is the Event Held?', max_length=255)),
                ('limit', models.IntegerField()),
                ('event', models.ForeignKey(related_name='event_room', to='events.Event')),
            ],
            options={
                'ordering': ('event', 'name', 'limit'),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='entry',
            name='event',
            field=models.ForeignKey(related_name='entry_event_association', to='events.Event'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='room',
            field=models.ForeignKey(related_name='entry_room_association', to='events.Room'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='entry',
            name='student',
            field=models.ForeignKey(related_query_name=b'student', related_name='event_student_association', to='charterclub.Student'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(related_name='question_answer_association', to='events.Question'),
            preserve_default=True,
        ),
    ]
