from .models import ChatApp
from django import forms


class ChatAppForm(forms.ModelForm):
    class Meta:
        model = ChatApp
        fields = ('msg_content',)
