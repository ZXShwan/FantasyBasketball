# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170510_2010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='is_win',
            field=models.CharField(default='pending', max_length=10, verbose_name='result'),
        ),
    ]