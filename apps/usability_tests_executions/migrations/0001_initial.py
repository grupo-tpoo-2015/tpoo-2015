# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0003_auto_20150917_1427'),
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractionStepExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('interaction_step', models.ForeignKey(to='tasks.InteractionStep')),
            ],
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('participant', models.ForeignKey(to='usability_tests_executions.Participant')),
                ('scenario', models.ForeignKey(to='usability_tests.Scenario')),
            ],
        ),
        migrations.CreateModel(
            name='TaskScenarioExecution',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scenario_execution', models.ForeignKey(to='usability_tests_executions.ScenarioExecution')),
                ('scenario_task', models.ForeignKey(to='tasks.ScenarioTask')),
            ],
        ),
        migrations.AddField(
            model_name='interactionstepexecution',
            name='task_scenario_execution',
            field=models.ForeignKey(to='usability_tests_executions.TaskScenarioExecution'),
        ),
    ]
