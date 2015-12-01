# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20151003_1858'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObservationType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('unit', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='interactionstep',
            name='observation_types',
            field=models.ManyToManyField(related_name='steps', to='tasks.ObservationType'),
        ),
    ]
