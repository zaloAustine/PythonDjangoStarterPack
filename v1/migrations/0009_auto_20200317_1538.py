# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-17 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0008_quiz_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='owner',
            field=models.CharField(max_length=300),
        ),
    ]
