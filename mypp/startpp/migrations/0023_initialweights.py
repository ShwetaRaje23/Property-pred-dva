# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startpp', '0022_citypropertydata'),
    ]

    operations = [
        migrations.CreateModel(
            name='InitialWeights',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
                ('area', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
                ('bedrooms', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
                ('crime', models.DecimalField(null=True, max_digits=100, decimal_places=9)),
            ],
        ),
    ]
