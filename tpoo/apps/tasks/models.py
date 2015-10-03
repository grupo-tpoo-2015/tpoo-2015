from django.db import models
from usability_tests.models import Scenario, Task, Refactoring


class ObservationType(models.Model):
    name = models.CharField(max_length=64)
    unit = models.CharField(max_length=20)


class ScenarioTask(models.Model):
    task = models.ForeignKey(Task)
    scenario = models.ForeignKey(Scenario, related_name='tasks')
    refactorings = models.ManyToManyField(Refactoring, related_name='scenario_tasks')


class InteractionStep(models.Model):
    scenario_task = models.ForeignKey(ScenarioTask, related_name='steps')
    name = models.CharField(max_length=256)
    order = models.PositiveSmallIntegerField()
    is_question = models.BooleanField(default=False)
    observation_types = models.ManyToManyField(ObservationType, related_name='steps')
