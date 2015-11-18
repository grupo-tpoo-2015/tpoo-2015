# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_remove_scenariotask_legacy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactionstep',
            name='legacy_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
