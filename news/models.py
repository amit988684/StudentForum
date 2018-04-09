# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class News(models.Model):
    news_details = models.CharField(max_length=80)

    def __str__(self):
        return self.news_details

