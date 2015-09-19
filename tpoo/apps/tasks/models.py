from django.db import models
from usability_tests.models import Scenario, Task


class ScenarioTask(models.Model):
    task = models.ForeignKey(Task)
    scenario = models.ForeignKey(Scenario, related_name='tasks')


class InteractionStep(models.Model):
    scenario_task = models.ForeignKey(ScenarioTask, related_name='steps')
