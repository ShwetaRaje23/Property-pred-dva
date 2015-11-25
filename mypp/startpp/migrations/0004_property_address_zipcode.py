# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0003_remove_property_address_zipcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address_zipcode',
            field=models.CharField(default=0, max_length=5),
            preserve_default=False,
        ),
    ]
