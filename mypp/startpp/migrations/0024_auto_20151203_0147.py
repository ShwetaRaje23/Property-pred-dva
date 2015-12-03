# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0023_initialweights'),
    ]

    operations = [
        migrations.AlterField(
            model_name='initialweights',
            name='id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
