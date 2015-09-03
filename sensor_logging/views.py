import datetime

from django.shortcuts import render
from sensor_logging.models import Sensor
from sensor_logging.forms import IdFilterForm


def main_view(request):
    # Create a response
    if request.method == 'POST':
        id_form = IdFilterForm(request.POST)
        if id_form.is_valid():
            id_selected = int(id_form.cleaned_data['sensor_id'])
            sensor_rows = Sensor.objects.all().filter(sensor_id=id_selected)
            mea_data_list = []
            datetime_list = []
            for each in sensor_rows:
                mea_data_list.append(each.sensor_data)
                datetime_list.append(datetime.datetime.combine(each.mea_date, each.mea_time))
                print(each.sensor_id, each.sensor_data, datetime.datetime.combine(each.mea_date, each.mea_time))

    else:
        id_form = IdFilterForm()

    return render(request, 'sensor_logging/base.html',{
        'form': id_form,
    })
