# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-23 19:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('c_id', models.IntegerField(primary_key=True, serialize=False)),
                ('semester', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('c_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='department',
            fields=[
                ('num_c_off', models.IntegerField()),
                ('dept_name', models.CharField(max_length=250)),
                ('d_id', models.IntegerField(primary_key=True, serialize=False)),
                ('d_logo', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='enrollments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cbrowser.course')),
            ],
        ),
        migrations.CreateModel(
            name='links',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.CharField(max_length=1000)),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cbrowser.course')),
            ],
        ),
        migrations.CreateModel(
            name='prof',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('p_id', models.IntegerField(primary_key=True, serialize=False)),
                ('p_pic', models.CharField(max_length=1000)),
                ('c_taken', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cbrowser.course')),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cbrowser.department')),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('name', models.CharField(max_length=250)),
                ('s_id', models.IntegerField(primary_key=True, serialize=False)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='enrollments',
            name='s_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cbrowser.student'),
        ),
        migrations.AddField(
            model_name='course',
            name='dept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cbrowser.department'),
        ),
    ]
