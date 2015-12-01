# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests_executions', '0002_observation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interactionstepexecution',
            name='task_scenario_execution',
            field=models.ForeignKey(related_name='steps', to='usability_tests_executions.TaskScenarioExecution'),
        ),
        migrations.AlterField(
            model_name='scenarioexecution',
            name='participant',
            field=models.ForeignKey(related_name='scenario_executions', to='usability_tests_executions.Participant'),
        ),
        migrations.AlterField(
            model_name='scenarioexecution',
            name='scenario',
            field=models.ForeignKey(related_name='executions', to='usability_tests.Scenario'),
        ),
        migrations.AlterField(
            model_name='taskscenarioexecution',
            name='scenario_execution',
            field=models.ForeignKey(related_name='scenario_task_executions', to='usability_tests_executions.ScenarioExecution'),
        ),
    ]
