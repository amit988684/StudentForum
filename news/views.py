# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# My added
from .models import News
from .forms import NewsForm
from django.views import generic
# Create your views here.


class NewsListView(generic.ListView):
    model = News
    template_name = 'home.html'


class NewsCreateView(generic.CreateView):
    model = News
    form_class = NewsForm

