# -*- coding: utf-8 -*-
# Generated by Django 1.10a1 on 2016-06-20 05:10
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('MyCalendar', '0003_auto_20160619_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='from_date_and_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 20, 5, 10, 13, 568368, tzinfo=utc), verbose_name='Start'),
        ),
    ]
