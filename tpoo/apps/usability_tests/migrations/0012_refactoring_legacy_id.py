# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0011_scenario_legacy_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='refactoring',
            name='legacy_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
