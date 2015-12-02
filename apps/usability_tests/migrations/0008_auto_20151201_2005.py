# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0007_sqldump'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usabilitytest',
            name='legacy_id',
        ),
        migrations.AddField(
            model_name='sqldump',
            name='is_the_current_one',
            field=models.BooleanField(default=False),
        ),
    ]
