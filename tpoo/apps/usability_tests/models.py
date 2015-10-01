from django.db import models
from django.contrib.auth.models import User


# esto en realidad es App
class UsabilityTest(models.Model):
    owner = models.ForeignKey(User, related_name='usability_tests')
    name = models.CharField(max_length=64)


class AppVersion(models.Model):
    name = models.CharField(max_length=64)
    usability_test = models.ForeignKey(UsabilityTest, related_name='versions')


class Refactoring(models.Model):
    name = models.CharField(max_length=64)   


class Task(models.Model):
    name = models.CharField(max_length=256)
    usability_test = models.ForeignKey(UsabilityTest, related_name='tasks')


class Scenario(models.Model):
    name = models.CharField(max_length=64)
    app_version = models.ForeignKey(AppVersion, related_name='scenarios')
