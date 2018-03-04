# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Question, Comment
# Register your models here.


# class QuestionAdmin(admin.ModelAdmin):
#     # list_display = ('author','title')
#     list_editable = ('title',)


# class CommentAdmin(admin.ModelAdmin):
#     list_display = ['question', 'timestamp_comment']

# admin.site.register(Question)

# admin.site.register(Question,QuestionAdmin)
admin.site.register(Question)
admin.site.register(Comment)
