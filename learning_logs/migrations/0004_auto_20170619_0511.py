# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-19 02:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_auto_20170618_0735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='date_added',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='topic',
            name='date_added',
            field=models.DateTimeField(),
        ),
    ]
