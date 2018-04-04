# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.


# I added
from .forms import EventForm
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView

class EventCreateView(CreateView):
    form_class = EventForm

