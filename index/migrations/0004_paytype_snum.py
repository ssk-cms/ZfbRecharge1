# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-14 12:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_goodtype_shop'),
    ]

    operations = [
        migrations.AddField(
            model_name='paytype',
            name='snum',
            field=models.IntegerField(default=1),
        ),
    ]