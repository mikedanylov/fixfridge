# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sensor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('sensor_id', models.IntegerField(default=0)),
                ('sensor_data', models.FloatField(default=0)),
                ('mea_date', models.DateField(verbose_name='date')),
                ('mea_time', models.TimeField(verbose_name='time')),
            ],
        ),
    ]
