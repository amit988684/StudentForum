from django import forms
from .models import Assignment,Slide
# from bootstrap3_datepicker.widgets import DatePickerInput


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignment_name','in_course','deadline','assignment_file','share','for_semester')


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ('slide_name', 'in_course', 'slide_file',)


class AssignmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignment_name','deadline', 'share')
