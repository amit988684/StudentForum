# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import (CreateView,TemplateView,ListView,DetailView)
from django.shortcuts import render
# Create your views here.

from braces.views import LoginRequiredMixin


# class ChatCreateView(LoginRequiredMixin,CreateView):

