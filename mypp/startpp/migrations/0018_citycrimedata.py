# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0017_citymiscservicesdata'),
    ]

    operations = [
        migrations.CreateModel(
            name='CityCrimeData',
            fields=[
                ('offense_id', models.IntegerField(serialize=False, primary_key=True)),
                ('location', models.CharField(max_length=140)),
                ('crime_type', models.CharField(max_length=140)),
                ('neighborhood', models.CharField(max_length=140)),
                ('location_lat', models.DecimalField(max_digits=100, decimal_places=9)),
                ('location_lng', models.DecimalField(max_digits=100, decimal_places=9)),
            ],
        ),
    ]
