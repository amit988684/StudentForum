from django import forms
from .models import Event
# from django.forms.extras.widgets import Widget
# from django.contrib.admin import widgets
# from django.forms.widgets import SplitDateTimeWidget
from django.forms.extras.widgets import SelectDateWidget
from bootstrap3_datetime.widgets import DateTimePicker
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit


# valid_time_formats = ['%P', '%H:%M%A', '%H:%M %A', '%H:%M%a', '%H:%M %a']
valid_time_formats = ['%H:%M', '%I:%M%p', '%I:%M %p']


class EventForm(forms.ModelForm):
    event_date = forms.DateTimeField(widget=SelectDateWidget)
    event_time = forms.TimeField(widget=DateTimePicker(options={
                                       "pickTime": True,
                                       "pickDate": False,
                                       "minuteStepping": 10,
                                       "sideBySide": True,
                                       },attrs={'type':'time'}),input_formats=valid_time_formats)

    class Meta:
        model = Event
        fields = ('event_name','event_details' , 'event_date', 'event_time', 'private',)


    #
    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         Fieldset(
    #             'event_name',
    #             'event_date',
    #             'event_time',
    #             'private',
    #             # 'favorite_food',
    #             # 'notes'
    #         ),
    #         ButtonHolder(
    #             Submit('submit', 'Submit', css_class='button white')
    #         )
    #     )
    #     super(EventForm, self).__init__(*args, **kwargs)

