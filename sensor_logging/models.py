from django.db import models
from django.utils.translation import ugettext_lazy as _


class Sensor(models.Model):

    sensor_id = models.IntegerField(default=0)
    sensor_data = models.FloatField(default=0)
    mea_date = models.DateField('date')
    mea_time = models.TimeField('time')

    class Meta:
        db_table = u'sensor_logging_sensor'
        verbose_name = _("Sensor")
        verbose_name_plural = _("Sensors")
        ordering = ("mea_date",)

    def __str__(self):
        return str(self.sensor_id) + ' ' +\
               str(self.sensor_data) + ' ' +\
               str(self.mea_date) + ' ' +\
               str(self.mea_time)