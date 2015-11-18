# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0010_task_legacy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenario',
            name='legacy_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
