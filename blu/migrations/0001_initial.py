# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 04:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='verification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ver_tok', models.CharField(max_length=200, verbose_name='Verification Token')),
                ('ver', models.IntegerField(verbose_name='Verification')),
                ('val_until', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Valid Until')),
                ('pay', models.CharField(max_length=200, verbose_name='Payload')),
                ('last_mod', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Last Modified')),
            ],
        ),
    ]
