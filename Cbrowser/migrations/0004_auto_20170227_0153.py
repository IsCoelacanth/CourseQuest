# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 20:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cbrowser', '0003_auto_20170227_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dp',
            field=models.CharField(default='', max_length=1000),
        ),
        migrations.AlterField(
            model_name='student',
            name='gpa',
            field=models.FloatField(default=0),
        ),
    ]
