# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_event_event_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_time',
            field=models.DateTimeField(null=True),
        ),
    ]
