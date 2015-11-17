# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0007_auto_20151117_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='sqldump',
            name='name',
            field=models.CharField(max_length=64, null=True, blank=True),
        ),
    ]
