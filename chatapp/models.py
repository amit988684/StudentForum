# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
# My Imports :
from django.conf import settings

# Create your models here.


class ChatApp(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, default=settings.AUTH_USER_MODEL,related_name='sender')
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='receiver')

    msg_content = models.TextField(max_length=1000,null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.msg_content)

