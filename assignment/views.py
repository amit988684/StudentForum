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
from django.contrib.auth.decorators import login_required


# List View
class AssignmentListView(LoginRequiredMixin, ListView):
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


class SlideListView(LoginRequiredMixin, ListView):
    model = Slide

    def get_queryset(self):
        return Slide.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SlideListView,self).get_context_data(**kwargs)
        context.update({
            'courses': Course.objects.all().order_by('course_id'),
            # 'assignment_list': Assignment.objects.all(),
        })
        return context

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

        self.object.slide_file = self.request.FILES['slide_file']

        self.object.save()
        return super(SlideCreateView,self).form_valid(form)


# Delete View
class AssignmentDeleteView(LoginRequiredMixin,DeleteView):
    model = Assignment
    success_url = reverse_lazy('assignment:assignment_list')


class SlideDeleteView(LoginRequiredMixin,DeleteView):
    model = Slide
    success_url = reverse_lazy('assignment:slide_list')


class AssignmentUpdateView(LoginRequiredMixin,UpdateView):
    model = Assignment
    form_class = AssignmentForm
    success_url = reverse_lazy('assignment:assignment_list')
    login_url = '/login/'


class SlideUpdateView(LoginRequiredMixin,UpdateView):
    model = Slide
    form_class = SlideForm
    success_url = reverse_lazy('assignment:slide_list')
    login_url = '/login/'

@login_required
def assignment_list_by_course(request,**kwargs):
    # print (kwargs)
    course_val = str(kwargs['course_val'])
    assignment_list = Assignment.objects.filter(in_course__course_id=course_val)
    courses = Course.objects.all()
    # print("amit" + query)
    return render(request,'assignment/assignment_list.html',{'assignment_list': assignment_list,'courses':courses})


@login_required
def slide_list_by_course(request,**kwargs):
    # print (kwargs)
    course_val = str(kwargs['course_val'])
    slide_list = Slide.objects.filter(in_course__course_id=course_val)
    courses = Course.objects.all()
    # print("amit" + query)
    return render(request,'assignment/slide_list.html',{'slide_list': slide_list,'courses':courses})

