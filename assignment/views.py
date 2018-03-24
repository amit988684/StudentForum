# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import (TemplateView,ListView
                                 ,DeleteView,DetailView
                                 ,UpdateView,CreateView,)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from django.shortcuts import render

# My Models and forms
from .models import Assignment,Slide
from .forms import AssignmentForm,SlideForm
# Create your views here.


# List View
class AssignmentListView(LoginRequiredMixin,ListView):
    model = Assignment

    def get_queryset(self):
        return Assignment.objects.all()


class SlideListView(LoginRequiredMixin,ListView):
    model = Slide

    def get_queryset(self):
        return Slide.objects.all()


# Create View
class AssignmentCreateView(LoginRequiredMixin,CreateView):
    model = Assignment
    form_class = AssignmentForm
    # redirect_field_name = ""

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploaded_by = self.request.user
        self.object.save()
        return super(AssignmentCreateView,self).form_valid(form)


class SlideCreateView(LoginRequiredMixin,CreateView):
    model = Slide
    form_class = SlideForm
    # redirect_field_name = ""

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploaded_by = self.request.user
        self.object.save()
        return super(SlideCreateView,self).form_valid(form)

# Delete View
class AssignmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Assignment
    # success_url =


class SlideDeleteView(LoginRequiredMixin,DeleteView):
    model = Slide
    # success_url =