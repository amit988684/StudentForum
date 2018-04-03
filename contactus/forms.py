from django import forms


class ContactUsForm(forms.Form):
    your_email = forms.EmailField(max_length=50)
    subject = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea(attrs={'style':'resize:none'}),max_length=150,required=True)


