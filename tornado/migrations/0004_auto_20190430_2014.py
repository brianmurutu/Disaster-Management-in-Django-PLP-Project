# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-30 20:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tornado', '0003_auto_20190430_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tornado',
            name='rotation',
            field=models.CharField(choices=[('Clock', 'ClockWise'), ('A-Clock', 'Anti Clockwise')], max_length=25),
        ),
    ]
