# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0004_auto_20150930_1914'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='refactoring',
            name='app_version',
        ),
    ]
