# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import (TemplateView,ListView
                                 ,DeleteView,DetailView
                                 ,UpdateView,CreateView,

                                  )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import get_object_or_404,redirect
from django.shortcuts import render

# My Models and forms
from .models import Assignment,Slide
from .forms import AssignmentForm,SlideForm
# Create your views here.
from django.db.models import Sum
from profiles.models import Course


# List View
class AssignmentListView(LoginRequiredMixin,ListView):
    model = Assignment

    def get_queryset(self):
        return Assignment.objects.all().order_by('in_course')

    def get_context_data(self, **kwargs):
        context = super(AssignmentListView,self).get_context_data(**kwargs)
        context.update({
            'courses': Course.objects.all().order_by('course_id'),
            # 'assignment_list': Assignment.objects.all(),
        })
        return context


class SlideListView(LoginRequiredMixin,ListView):
    model = Slide

    def get_queryset(self):
        return Slide.objects.all()


# Create View
class AssignmentCreateView(LoginRequiredMixin,CreateView):
    model = Assignment
    form_class = AssignmentForm
    redirect_field_name = "assignment_list.html"


    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.uploaded_by = self.request.user

        self.object.assignment_file = self.request.FILES['assignment_file']

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
    success_url = reverse_lazy('assignment:assignment_list')


class SlideDeleteView(LoginRequiredMixin,DeleteView):
    model = Slide
    # success_url =


class AssignmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = reverse_lazy('assignment:assignment_list')
    login_url = '/login/'


