# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-15 09:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_basicrecord_loss'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicrecord',
            name='income',
            field=models.IntegerField(default=0),
        ),
    ]
