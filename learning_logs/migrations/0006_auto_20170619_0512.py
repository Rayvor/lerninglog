# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 02:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_topic_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 2, 12, 5, 757559, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 19, 2, 12, 5, 757559, tzinfo=utc)),
        ),
    ]
