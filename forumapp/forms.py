from django import forms
from .models import Comment,Question


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class QuestionForm(forms.ModelForm):
    content = forms.CharField(max_length=1000,widget=forms.Textarea)
    class Meta:
        model = Question
        fields = ('title', 'content',)

