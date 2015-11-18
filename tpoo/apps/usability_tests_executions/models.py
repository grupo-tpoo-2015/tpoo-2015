# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from usability_tests.models import Scenario, SqlDump
from tasks.models import ScenarioTask, InteractionStep, ObservationType


class Participant(models.Model):
    name = models.CharField(max_length=64)
    dump = models.ForeignKey(SqlDump, null=True, blank=True)    

    def __unicode__(self):
        return self.name


class ScenarioExecution(models.Model):
    scenario = models.ForeignKey(Scenario, related_name='executions')
    participant = models.ForeignKey(Participant, related_name='scenario_executions')

    def __unicode__(self):
        return "Ejecución del scenario %d por parte del participante %d" % (
            self.scenario_id,
            self.participant_id,
        )


class TaskScenarioExecution(models.Model):
    scenario_execution = models.ForeignKey(ScenarioExecution,
                                           related_name='scenario_task_executions')
    scenario_task = models.ForeignKey(ScenarioTask)

    def __unicode__(self):
        return "Ejecución de la tarea %d en el escenario %d" % (
            self.scenario_task_id,
            self.scenario_execution_id,
        )


class InteractionStepExecution(models.Model):
    task_scenario_execution = models.ForeignKey(TaskScenarioExecution, related_name='steps')
    interaction_step = models.ForeignKey(InteractionStep)

    def __unicode__(self):
        return "Ejecución del step %d para la tarea-escenario %d" % (
            self.interaction_step_id,
            self.task_scenario_execution_id,
        )


class Observation(models.Model):
    value = models.FloatField()
    step_execution = models.ForeignKey(InteractionStepExecution, related_name='observations')
    observation_type = models.ForeignKey(ObservationType, related_name='observations')

    def __unicode__(self):
        return "%.2f" % self.value