# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from profiles.models import Course

# Create your models here.


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,default=settings.AUTH_USER_MODEL)
    in_course = models.ForeignKey(Course,null=True,blank=True)
    deadline = models.DateField(blank=True,null=True)

    assignment_file = models.FileField('Assignment', upload_to='assignment', null=True)
    # resume = models.FileField('Teacher Resume', upload_to='resume', null=True, blank=True)

    def __str__(self):
        return self.assignment_name

    def __unicode__(self):
        return self.assignment_name

    class Meta:
        ordering = ['-deadline']


class Slide(models.Model):
    slide_name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=settings.AUTH_USER_MODEL)
    in_course = models.ForeignKey(Course, null=True, blank=True)
    # deadline = models.DateField(blank=True, null=True)

    slide_file = models.FileField('Slide', upload_to='slide', null=True)

    def __str__(self):
        return self.slide_name

    def __unicode__(self):
        return self.slide_name

    class Meta:
        ordering = ['-pk']