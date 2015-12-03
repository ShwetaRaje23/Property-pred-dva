# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0020_citypropertydata_temp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='citypropertydata_temp',
            old_name='price',
            new_name='price_input',
        ),
    ]
