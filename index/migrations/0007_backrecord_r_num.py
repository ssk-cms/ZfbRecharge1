# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-15 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_auto_20181214_2100'),
    ]

    operations = [
        migrations.AddField(
            model_name='backrecord',
            name='r_num',
            field=models.IntegerField(default=0),
        ),
    ]
