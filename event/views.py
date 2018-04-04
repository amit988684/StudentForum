# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# Create your views here.

# I added
from .forms import EventForm
from .models import Event
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404,redirect


class EventCreateView(LoginRequiredMixin,CreateView):
    model = Event
    form_class = EventForm


class EventListView(LoginRequiredMixin,ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()


class EventDeleteView(LoginRequiredMixin,DeleteView):
    model = Event
    success_url = reverse_lazy('event:event_list')


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event:event_list')
    login_url = '/login/'

