# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0009_refactoring_dump'),
        ('usability_tests_executions', '0003_auto_20151008_1231'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='dump',
            field=models.ForeignKey(blank=True, to='usability_tests.SqlDump', null=True),
        ),
    ]
