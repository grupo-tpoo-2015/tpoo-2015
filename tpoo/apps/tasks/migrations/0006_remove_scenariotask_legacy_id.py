# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_scenariotask_legacy_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scenariotask',
            name='legacy_id',
        ),
    ]
