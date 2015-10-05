from django.db import models
from django.contrib.auth.models import User


# esto en realidad es App
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

