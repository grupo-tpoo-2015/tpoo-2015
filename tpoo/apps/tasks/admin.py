from django.contrib import admin
from tasks.models import ObservationType, ScenarioTask, InteractionStep


admin.site.register(ObservationType)
admin.site.register(ScenarioTask)
admin.site.register(InteractionStep)