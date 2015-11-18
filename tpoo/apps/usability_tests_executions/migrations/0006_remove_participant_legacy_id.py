# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests_executions', '0005_participant_legacy_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='legacy_id',
        ),
    ]
