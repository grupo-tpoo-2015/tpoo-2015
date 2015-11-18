# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0008_sqldump_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='refactoring',
            name='dump',
            field=models.ForeignKey(blank=True, to='usability_tests.SqlDump', null=True),
        ),
    ]
