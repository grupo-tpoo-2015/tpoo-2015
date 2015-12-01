# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_scenariotask_refactorings'),
    ]

    operations = [
        migrations.AddField(
            model_name='interactionstep',
            name='is_question',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='interactionstep',
            name='name',
            field=models.CharField(default='a', max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='interactionstep',
            name='order',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
