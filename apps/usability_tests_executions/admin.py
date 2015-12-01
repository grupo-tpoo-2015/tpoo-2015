from django.contrib import admin
from usability_tests_executions.models import (
    Participant,
    ScenarioExecution,
    TaskScenarioExecution,
    InteractionStepExecution,
    Observation,
)

admin.site.register(Participant)
admin.site.register(ScenarioExecution)
admin.site.register(TaskScenarioExecution)
admin.site.register(InteractionStepExecution)
admin.site.register(Observation)
