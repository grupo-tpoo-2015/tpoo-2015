from django.db import models
from django.contrib.auth.models import User


class UsabilityTest(models.Model):

    owner = models.ForeignKey(User)
    name = models.CharField(max_length=64)
