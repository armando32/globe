# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 04:43
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Globe_Mobile_Admin', '0005_auto_20160524_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='Session_expiry',
            field=models.DateTimeField(default=datetime.datetime(2016, 7, 23, 4, 43, 8, 943234, tzinfo=utc), verbose_name='Session expiry'),
        ),
    ]
