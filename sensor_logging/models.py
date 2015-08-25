from django.db import models
from django.utils import timezone

# Create your models here.


class Sensor(models.Model):

    sensor_id = models.IntegerField(default=0)
    sensor_data = models.FloatField(default=0)
    mea_date = models.DateField('date')
    mea_time = models.TimeField('time')

    def __str__(self):
        return self.sensor_id