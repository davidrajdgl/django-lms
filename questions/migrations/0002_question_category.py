# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-10 15:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.CharField(default='Examples', max_length=30),
            preserve_default=False,
        ),
    ]