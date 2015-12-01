# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0005_remove_refactoring_app_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='usabilitytest',
            name='legacy_id',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
