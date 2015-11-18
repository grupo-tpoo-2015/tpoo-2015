# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0009_refactoring_dump'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='legacy_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
