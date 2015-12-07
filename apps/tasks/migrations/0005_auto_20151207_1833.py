# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20151003_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interactionstep',
            options={'ordering': ['order']},
        ),
    ]
