# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 20:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='uploaded_by',
            field=models.ForeignKey(default=b'authtools.User', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
