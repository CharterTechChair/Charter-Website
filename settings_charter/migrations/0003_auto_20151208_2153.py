# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('settings_charter', '0002_auto_20151208_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='charterclubsettings',
            old_name='default_house_account_for_new_account',
            new_name='default_house_account_for_new_member',
        ),
    ]
