__author__ = 'mikedanylov'

from django import forms
from crispy_forms.helper import FormHelper

from sensor_logging.models import Sensor


class IdFilterForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['sensor_id']

    def __init__(self, *args, **kwargs):
        super(IdFilterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"

        id_choices = get_sensor_ids(self)
        self.fields['sensor_id'] = forms.ChoiceField(choices=id_choices, label='Sensor ID', initial='')


class DateFilterForm(forms.ModelForm):
    class Meta:
        model = Sensor
        fields = ['mea_date']

    def __init__(self, *args, **kwargs):
        super(DateFilterForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_action = ""
        self.helper.form_method = "POST"


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
