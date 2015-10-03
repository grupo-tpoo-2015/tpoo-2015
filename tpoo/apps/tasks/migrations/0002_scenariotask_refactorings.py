# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0005_remove_refactoring_app_version'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='scenariotask',
            name='refactorings',
            field=models.ManyToManyField(related_name='scenario_tasks', to='usability_tests.Refactoring'),
        ),
    ]
