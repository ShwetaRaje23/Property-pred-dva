# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0018_citycrimedata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citycrimedata',
            name='offense_id',
            field=models.BigIntegerField(serialize=False, primary_key=True),
        ),
    ]
