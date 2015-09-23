import datetime
import time

from django.shortcuts import render, redirect
from sensor_logging.models import Sensor
from sensor_logging import forms
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt


def main_view(request):
    # if request.method == 'POST':
    #     id_form = forms.IdFilterForm(request.POST)
    # else:
    #     id_form = forms.IdFilterForm()
    # return render(request, 'sensor_logging/base.html',{
    #     'form': id_form,
    # })
    return redirect('/realtime')


def home_view(request):
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


@csrf_exempt
def realtime_view(request):
    if request.method == 'POST' and request.is_ajax():
        data = dict(request.POST)
        id = data['sensor_id'][0]
        time_frame = int(data['time_frame'][0])
        time_begin = time.time() - time_frame * 3600
        sensor_rows = Sensor.objects.filter(sensor_id=id)
        sensor_mea = []
        sensor_datetime = []
        for each in sensor_rows:
            datetime_millis = time.mktime(
                datetime.datetime.combine(each.mea_date, each.mea_time).timetuple()
            )
            if datetime_millis > time_begin:  # append only if within time frame
                sensor_datetime.append(datetime_millis)
                sensor_mea.append(each.sensor_data)
        new_data = {}
        new_data["mea_value"] = sensor_mea
        new_data["mea_datetime"] = sensor_datetime
        return JsonResponse(new_data)
    return render(request, 'sensor_logging/real_time_filter.html')


def oldlogs_view(request):
    return render(request, 'sensor_logging/old_logs_filter.html')