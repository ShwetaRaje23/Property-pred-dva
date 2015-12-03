# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0019_auto_20151129_1947'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityPropertyData_temp',
            fields=[
                ('id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('num_bedrooms', models.BigIntegerField()),
                ('location', models.CharField(max_length=140)),
                ('price', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
                ('location_lat', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
                ('location_lng', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
            ],
        ),
    ]
