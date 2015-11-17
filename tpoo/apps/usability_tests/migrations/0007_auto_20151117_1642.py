# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usability_tests', '0006_usabilitytest_legacy_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='SqlDump',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('script_file', models.FileField(upload_to=b'dumps')),
                ('uploaded_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usabilitytest',
            name='dump',
            field=models.ForeignKey(blank=True, to='usability_tests.SqlDump', null=True),
        ),
    ]
