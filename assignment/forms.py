from django import forms
from .models import Assignment,Slide


class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ('assignment_name','in_course','deadline','assignment_file',)


class SlideForm(forms.ModelForm):
    class Meta:
        model = Slide
        fields = ('slide_name', 'in_course', 'slide_file',)


