from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Div, HTML
from crispy_forms import layout
from crispy_forms import bootstrap
from crispy_forms.bootstrap import StrictButton

from sensor_logging.models import Sensor

__author__ = 'mikedanylov'


class IdFilterForm(forms.Form):
    class Meta:
        model = Sensor
        fields = ['sensor_id']

    def __init__(self, *args, **kwargs):
        super(IdFilterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        id_choices = get_sensor_ids(self)
        self.fields['sensor_id'] = forms.ChoiceField(choices=id_choices, label='Sensor ID', initial='1')


# class DateFilterForm(forms.ModelForm):
#     class Meta:
#         model = Sensor
#         fields = ['mea_date']
#
#     def __init__(self, *args, **kwargs):
#         super(DateFilterForm, self).__init__(*args, **kwargs)
#
#         self.helper = FormHelper()
#         self.helper.form_action = ""
#         self.helper.form_method = "POST"


def get_sensor_ids(form):
    '''
    get unique sensor ids from db
    :return:
    list of tuples [(1, 1), (2, 2),]
    '''
    raw_choices = Sensor.objects.values_list(form.Meta.fields[0], form.Meta.fields[0]).distinct()

    cleaned_choices = []
    for raw_choice in raw_choices:
        if raw_choice not in cleaned_choices:
            cleaned_choices.append(raw_choice)

    return cleaned_choices


class MainPageForm(forms.Form):

    helper = FormHelper()
    helper.form_action = ''
    helper.form_class = 'form-horizontal'
    helper.form_method = 'POST'

    helper.layout = Layout(
        Div(
            Submit('btn-real-time', 'real-time', css_class="btn btn-success btn-lg col-xs-offset-3 col-md-offset-3 col-lg-offset-4"),
            Submit('btn-old-logs', '  old logs  ', css_class="btn btn-warning btn-lg col-xs-offset-2 col-sm-offset-2 col-md-offset-3 col-lg-offset-2"),
        )
    )


# class RealtimeFilterForm(forms.Form):

