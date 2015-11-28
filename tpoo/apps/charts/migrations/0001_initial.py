# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usability_tests', '0007_sqldump'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChartCachedData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=2)),
                ('data', models.TextField()),
                ('usability_test', models.ForeignKey(blank=True, to='usability_tests.UsabilityTest', null=True)),
            ],
        ),
    ]
