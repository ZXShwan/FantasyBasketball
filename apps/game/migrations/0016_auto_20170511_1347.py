# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-11 18:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0015_auto_20170511_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='hour',
            field=models.CharField(default=b'13:47', max_length=20, verbose_name='Hour'),
        ),
    ]
