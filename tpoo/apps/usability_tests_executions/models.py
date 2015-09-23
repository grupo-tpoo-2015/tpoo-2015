from django.db import models
from usability_tests.models import Scenario
from tasks.models import ScenarioTask, InteractionStep


# Create your models here.
class Participant(models.Model):
    name = models.CharField(max_length=64)


class ScenarioExecution(models.Model):
    scenario = models.ForeignKey(Scenario)
    participant = models.ForeignKey(Participant)


class TaskScenarioExecution(models.Model):
    scenario_execution = models.ForeignKey(ScenarioExecution)
    scenario_task = models.ForeignKey(ScenarioTask)


class InteractionStepExecution(models.Model):
    task_scenario_execution = models.ForeignKey(TaskScenarioExecution)
    interaction_step = models.ForeignKey(InteractionStep)
