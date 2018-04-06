from django import forms
from .models import Event
# from django.forms.extras.widgets import Widget
# from django.contrib.admin import widgets
# from django.forms.widgets import SplitDateTimeWidget
from django.forms.extras.widgets import SelectDateWidget
from bootstrap3_datetime.widgets import DateTimePicker
# from bootstrap3.forms im

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


# valid_time_formats = ['%P', '%H:%M%A', '%H:%M %A', '%H:%M%a', '%H:%M %a']
# valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']


class EventForm(forms.ModelForm):
    # event_date = forms.DateTimeField(widget=SelectDateWidget)
    event_date_time = forms.DateTimeField(widget=DateTimePicker(options={
                                       "pickTime": True,
                                       "pickDate": True,
                                       "minuteStepping": 5,
                                       "sideBySide": True,
                                       }, attrs={'id': 'datetimepicker', 'class': 'date input-append'}))

    class Meta:
        model = Event
        fields = ('event_name', 'event_details', 'event_date_time', 'private',)

