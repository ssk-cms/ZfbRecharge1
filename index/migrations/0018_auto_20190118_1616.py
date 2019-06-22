# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2019-01-18 08:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0017_auto_20190116_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicrecord',
            name='updater',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shop',
            name='boss',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]