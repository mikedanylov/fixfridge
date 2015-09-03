# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sensor_logging', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sensor',
            options={'verbose_name_plural': 'Sensors', 'verbose_name': 'Sensor', 'ordering': ('mea_date',)},
        ),
        migrations.AlterModelTable(
            name='sensor',
            table='sensor_logging_sensor',
        ),
    ]
