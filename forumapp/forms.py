from django import forms
from .models import Comment,Question
from django.core import validators


# Block Offensive Words Validator
def block_offensive_words(value):
    offensive_words = ['fuck','dickhole','dick','sex','fuckyou','bitch','idiot',]
    temp = value.split(" ")
    for i in temp:
        if i in offensive_words:
            raise forms.ValidationError("You Cannot post with BAD WORDS")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)


class QuestionForm(forms.ModelForm):
    content = forms.CharField(max_length=1000,widget=forms.Textarea,validators=[block_offensive_words,])
    class Meta:
        model = Question
        fields = ('title', 'content',)
