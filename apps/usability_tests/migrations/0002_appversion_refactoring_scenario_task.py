# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppVersion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('usability_test', models.ForeignKey(to='usability_tests.UsabilityTest')),
            ],
        ),
        migrations.CreateModel(
            name='Refactoring',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('app_version', models.ForeignKey(to='usability_tests.AppVersion')),
            ],
        ),
        migrations.CreateModel(
            name='Scenario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('app_version', models.ForeignKey(to='usability_tests.AppVersion')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('usability_test', models.ForeignKey(to='usability_tests.UsabilityTest')),
            ],
        ),
    ]
