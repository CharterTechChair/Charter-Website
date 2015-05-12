# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150512_0359'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ('title',)},
        ),
        migrations.AlterModelOptions(
            name='seating',
            options={'ordering': ('member',)},
        ),
    ]
