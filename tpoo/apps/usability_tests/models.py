from django.db import models
from django.contrib.auth.models import User


class SqlDump(models.Model):
    name = models.CharField(max_length=64, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User)
    script_file = models.FileField(upload_to='dumps')


class UsabilityTest(models.Model):
    owner = models.ForeignKey(User, related_name='usability_tests')
    name = models.CharField(max_length=64)
    legacy_id = models.PositiveSmallIntegerField(default=0)

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

