# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-18 04:35
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0002_entry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 18, 4, 35, 14, 793705, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(verbose_name=datetime.datetime(2017, 6, 18, 4, 35, 14, 793705, tzinfo=utc)),
        ),
    ]