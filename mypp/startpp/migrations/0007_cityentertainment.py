# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0006_cityschools'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityEntertainment',
            fields=[
                ('name', models.CharField(max_length=140)),
                ('vicinity', models.CharField(max_length=140)),
                ('location_lat', models.DecimalField(max_digits=100, decimal_places=9)),
                ('location_lng', models.DecimalField(max_digits=100, decimal_places=9)),
                ('icon', models.CharField(max_length=300)),
                ('id', models.CharField(max_length=256)),
                ('place_id', models.CharField(max_length=256, serialize=False, primary_key=True)),
            ],
        ),
    ]
