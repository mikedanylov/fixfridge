import datetime
import time

from django.shortcuts import render, redirect
from sensor_logging.models import Sensor
from sensor_logging import forms


def main_view(request):
    # Create a response
    if request.method == 'POST':
        id_form = forms.IdFilterForm(request.POST)
        if id_form.is_valid():
            id_selected = int(id_form.cleaned_data['sensor_id'])
            sensor_rows = Sensor.objects.all().filter(sensor_id=id_selected)
            f_measurements = open('sensor_logging/static/measurements.txt','w')
            f_datetime = open('sensor_logging/static/datetime.txt','w')
            for each in sensor_rows:
                f_measurements.write(str(each.sensor_data) + ' ')
                datetime_millis = time.mktime(datetime.datetime.combine(each.mea_date, each.mea_time).timetuple())
                f_datetime.write(str(datetime_millis) + ' ')
    else:
        id_form = forms.IdFilterForm()
    return render(request, 'sensor_logging/base.html',{
        'form': id_form,
    })


def home_view(request):
    # Create a response
    if request.method == 'POST':
        main_form = forms.MainPageForm(request.POST)
        if main_form.is_valid():
            if 'btn-real-time' in request.POST:
                return redirect('/realtime/')
            elif 'btn-old-logs' in request.POST:
                return redirect('/oldlogs/')
    else:
        main_form = forms.MainPageForm()
    return render(request, 'sensor_logging/home.html',{
        'main_form': main_form,
    })


def realtime_view(request):
    # if request.method == 'POST':

    return render(request, 'sensor_logging/real_time_filter.html')


def oldlogs_view(request):
    # if request.method == 'POST':

    return render(request, 'sensor_logging/old_logs_filter.html')