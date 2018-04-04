from django import forms
from .models import Event
# from django.forms.extras.widgets import Widget
# from django.contrib.admin import widgets
# from django.forms.widgets import SplitDateTimeWidget
from django.forms.extras.widgets import SelectDateWidget
from bootstrap3_datetime.widgets import DateTimePicker


valid_time_formats = ['%P', '%H:%M%A', '%H:%M %A', '%H:%M%a', '%H:%M %a']


class EventForm(forms.ModelForm):
    event_date = forms.DateTimeField(widget=SelectDateWidget)
    event_time = forms.TimeField(widget=DateTimePicker(options={
                                   "pickTime": True,
                                   "pickDate": False,
                                   "minuteStepping": 1,
                                   "sideBySide": True,
                                   }),input_formats=valid_time_formats)

    class Meta:
        model = Event
        fields = ('event_name', 'event_date', 'event_time','private',)
