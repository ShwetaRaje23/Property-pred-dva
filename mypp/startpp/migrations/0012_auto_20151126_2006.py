# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0011_cityplacesofworship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cityplacesofworship',
            name='vicinity',
            field=models.CharField(max_length=140, null=True),
        ),
    ]
