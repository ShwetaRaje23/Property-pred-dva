# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0002_auto_20151113_2255'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='address_zipcode',
        ),
    ]
