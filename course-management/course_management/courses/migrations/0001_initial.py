# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-24 13:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=30)),
                ('start_date', models.DateField(max_length=30)),
                ('end_date', models.DateField(max_length=30)),
                ('approximation', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('lection_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('week', models.CharField(max_length=30)),
                ('url', models.CharField(max_length=30)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.Course')),
            ],
        ),
    ]
