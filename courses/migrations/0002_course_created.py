# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 1, 7, 9, 4, 15, 980970, tzinfo=utc)),
            preserve_default=False,
        ),
    ]