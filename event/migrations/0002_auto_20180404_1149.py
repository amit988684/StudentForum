# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-04 06:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='event_date',
            new_name='event_date_time',
        ),
    ]
