# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-08-03 19:34
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190801_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 3, 19, 34, 30, 166999, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 3, 19, 34, 30, 165995, tzinfo=utc)),
        ),
    ]
