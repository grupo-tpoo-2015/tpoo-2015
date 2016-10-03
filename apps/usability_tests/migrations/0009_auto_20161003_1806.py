# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0008_auto_20151201_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='refactoring',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
