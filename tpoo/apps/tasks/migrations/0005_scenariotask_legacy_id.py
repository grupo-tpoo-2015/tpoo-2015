# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20151003_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariotask',
            name='legacy_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
