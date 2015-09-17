# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0002_appversion_refactoring_scenario_task'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appversion',
            name='usability_test',
            field=models.ForeignKey(related_name='versions', to='usability_tests.UsabilityTest'),
        ),
        migrations.AlterField(
            model_name='refactoring',
            name='app_version',
            field=models.ForeignKey(related_name='refactorings', to='usability_tests.AppVersion'),
        ),
        migrations.AlterField(
            model_name='scenario',
            name='app_version',
            field=models.ForeignKey(related_name='scenarios', to='usability_tests.AppVersion'),
        ),
        migrations.AlterField(
            model_name='task',
            name='usability_test',
            field=models.ForeignKey(related_name='tasks', to='usability_tests.UsabilityTest'),
        ),
        migrations.AlterField(
            model_name='usabilitytest',
            name='owner',
            field=models.ForeignKey(related_name='usability_tests', to=settings.AUTH_USER_MODEL),
        ),
    ]
