# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render,redirect
from .forms import ContactUsForm
from django.views.generic import FormView
from django.core.mail import send_mail, BadHeaderError
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
# from django.core.mail import EmailMessage

# Create your views here.

class ContactUsView(FormView):
    form_class = ContactUsForm
    template_name = 'contactus_form.html'

    def form_valid(self, form):
        EmailFrom = form.cleaned_data['your_email']
        EmailTo = [settings.EMAIL_HOST_USER]
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['content']
        message = "%s %s %s %s " % ("message from :",EmailFrom,"\n Content : ", message)
        # print (from_mail,to_mail,subject,message)
        send_mail(subject,message,EmailFrom,EmailTo,fail_silently=True)

        return redirect('contactus:contactus_view')

#
# def SuccessView(request):
#     return reverse('contactus:contactus_view')


