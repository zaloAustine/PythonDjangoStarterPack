# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-17 11:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0002_auto_20200317_1033'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(default=565656, on_delete=django.db.models.deletion.CASCADE, to='v1.Quiz'),
            preserve_default=False,
        ),
    ]
