# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20151003_2003'),
        ('usability_tests_executions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Observation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('value', models.FloatField()),
                ('observation_type', models.ForeignKey(related_name='observations', to='tasks.ObservationType')),
                ('step_execution', models.ForeignKey(related_name='observations', to='usability_tests_executions.InteractionStepExecution')),
            ],
        ),
    ]
