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

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.event_by = self.request.user
        self.object.save()
        return super(EventCreateView,self).form_valid(form)



class EventListView(LoginRequiredMixin, ListView):
    model = Event

    def get_queryset(self):
        return Event.objects.all()

    def get_context_data(self, **kwargs):
        context = super(EventListView, self).get_context_data(**kwargs)
        # event_user= Event.objects.filter(event_by=self.request.user)
        context.update({
            'event_user': Event.objects.filter(event_by=self.request.user).first()
            # 'assignment_list': Assignment.objects.all(),
        })
        return context

class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Event
    success_url = reverse_lazy('event:event_list')


class EventUpdateView(UpdateView):
    model = Event
    form_class = EventForm
    success_url = reverse_lazy('event:event_list')
    login_url = '/login/'


def event_list_view_public(request):
    event_list = Event.objects.filter(private=False)
    context = {'event_list': event_list, }
    return render(request,'event/event_list_public.html', context=context)
