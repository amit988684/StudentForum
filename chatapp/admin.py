# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import ChatApp
# Register your models here.


class ChatAppAdmin(admin.ModelAdmin):
    list_display = ('sender','receiver','msg_content')

admin.site.register(ChatApp,ChatAppAdmin)