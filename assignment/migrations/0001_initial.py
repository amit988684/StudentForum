# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 20:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('profiles', '0003_auto_20180304_1033'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assignment_name', models.CharField(max_length=50)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('assignment_file', models.FileField(null=True, upload_to='assignment', verbose_name='Assignment')),
                ('in_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='profiles.Course')),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-deadline'],
            },
        ),
    ]
