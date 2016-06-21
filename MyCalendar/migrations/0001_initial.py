# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-21 03:28
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=255)),
                ('start_date', models.DateField(default=datetime.date(2016, 6, 21), null=True)),
                ('start_time', models.TimeField(null=True)),
                ('end_date', models.DateField(default=datetime.date(2016, 6, 21), null=True)),
                ('end_time', models.TimeField(null=True)),
                ('description', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('website', models.URLField(blank=True)),
                ('picture', models.ImageField(blank=True, upload_to='profile_images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='MyCalendar.UserProfile'),
        ),
    ]
