# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from usability_tests.models import UsabilityTest


class ChartCachedData(models.Model):
    type = models.PositiveSmallIntegerField()
    data = models.TextField()
    usability_test = models.ForeignKey(UsabilityTest, blank=True, null=True)
