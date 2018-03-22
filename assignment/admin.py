# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Assignment
# Register your models here.


class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('assignment_name', 'in_course', 'deadline')


admin.site.register(Assignment, AssignmentAdmin)


