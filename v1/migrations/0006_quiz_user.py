# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-17 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0005_auto_20200317_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='user',
            field=models.IntegerField(default=34352),
            preserve_default=False,
        ),
    ]
