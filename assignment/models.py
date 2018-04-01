# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from django.conf import settings

from profiles.models import Course

# Create your models here.


class Assignment(models.Model):
    assignment_name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL,default=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    in_course = models.ForeignKey(Course,null=True,blank=True,related_name='in_course')
    deadline = models.DateField(blank=True,null=True)

    share = models.BooleanField(default=False)
    for_semester = models.IntegerField(null=True,blank=True)

    assignment_file = models.FileField('Assignment', upload_to='assignment/%Y/%m/%d/', null=True)
    # resume = models.FileField('Teacher Resume', upload_to='resume', null=True, blank=True)

    def __str__(self):
        return str(self.assignment_name)

    def __unicode__(self):
        return str(self.assignment_name)

    # def share_assignment(self):
    #     self.share = True
    #     return self.share

    def get_absolute_url(self):
        return reverse('assignment:assignment_list')

    class Meta:
        ordering = ['-deadline']



class Slide(models.Model):
    slide_name = models.CharField(max_length=50)
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=settings.AUTH_USER_MODEL)
    in_course = models.ForeignKey(Course, null=True, blank=True)
    # deadline = models.DateField(blank=True, null=True)
    share = models.BooleanField(default=False)
    for_semester = models.IntegerField(null=True,blank=True)

    slide_file = models.FileField('Slide', upload_to='slide', null=True)

    def __str__(self):
        return self.slide_name

    def __unicode__(self):
        return self.slide_name

    def get_absolute_url(self):
        return reverse('assignment:slide_list')

    class Meta:
        ordering = ['-pk']