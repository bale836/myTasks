# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-19 14:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inf', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='createTime',
            field=models.DateTimeField(auto_now=True, verbose_name='createTime'),
        ),
    ]
