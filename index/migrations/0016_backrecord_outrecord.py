# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-21 11:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0015_auto_20181221_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='backrecord',
            name='outrecord',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='index.OutRecord'),
        ),
    ]
