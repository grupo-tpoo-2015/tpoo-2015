from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from subprocess import call


class UsabilityTest(models.Model):
    owner = models.ForeignKey(User, related_name='usability_tests')
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class AppVersion(models.Model):
    name = models.CharField(max_length=64)
    usability_test = models.ForeignKey(UsabilityTest, related_name='versions')

    def __unicode__(self):
        return self.name


class Refactoring(models.Model):
    name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length=256)
    usability_test = models.ForeignKey(UsabilityTest, related_name='tasks')

    def __unicode__(self):
        return self.name


class Scenario(models.Model):
    name = models.CharField(max_length=64)
    app_version = models.ForeignKey(AppVersion, related_name='scenarios')

    def __unicode__(self):
        return self.name


class SqlDump(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User)
    script_file = models.FileField(upload_to='dumps')
    is_the_current_one = models.BooleanField(default=False)

    def choose(self):
        from charts.charts import CompareTaskBetweenVersionsChart
        call(["/bin/bash", settings.BASE_DIR + "/load.sh", self.script_file.path])
        SqlDump.objects.update(is_the_current_one=False)
        self.is_the_current_one = True
        self.save()
        # this forces data for these charts to be cached
        for ut in UsabilityTest.objects.all():
            CompareTaskBetweenVersionsChart(ut).as_dict()
