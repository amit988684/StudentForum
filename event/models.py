# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=50)
    event_date = models.DateField(null=True)
    event_time = models.TimeField(null=True)

    event_added_on = models.DateTimeField(auto_now_add=True)
    event_by = models.ForeignKey(settings.AUTH_USER_MODEL,default=settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    private = models.BooleanField(default=True)

    def __str__(self):
        return self.event_name

    def __unicode__(self):
        return self.event_name

    class Meta:
        ordering = ['event_date', 'event_time',]