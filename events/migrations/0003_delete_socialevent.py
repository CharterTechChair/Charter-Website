# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_delete_menuitem'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SocialEvent',
        ),
    ]
