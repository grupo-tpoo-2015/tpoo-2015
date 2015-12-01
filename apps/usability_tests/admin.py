from django.contrib import admin
from .models import UsabilityTest, Task, Refactoring, Scenario, AppVersion


admin.site.register(UsabilityTest)
admin.site.register(Task)
admin.site.register(Refactoring)
admin.site.register(Scenario)
admin.site.register(AppVersion)
