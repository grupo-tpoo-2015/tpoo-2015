# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0003_auto_20150917_1427'),
    ]

    operations = [
        migrations.CreateModel(
            name='InteractionStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='ScenarioTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('scenario', models.ForeignKey(related_name='tasks', to='usability_tests.Scenario')),
                ('task', models.ForeignKey(to='usability_tests.Task')),
            ],
        ),
        migrations.AddField(
            model_name='interactionstep',
            name='scenario_task',
            field=models.ForeignKey(related_name='steps', to='tasks.ScenarioTask'),
        ),
    ]
