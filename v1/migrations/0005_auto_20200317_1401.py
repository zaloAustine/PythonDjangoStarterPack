# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-03-17 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('v1', '0004_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(verbose_name='question')),
                ('second_name', models.TextField(verbose_name='choice1')),
                ('email', models.TextField(verbose_name='choise2')),
                ('phone', models.TextField(verbose_name='choise3')),
                ('image', models.TextField(verbose_name='correct answer')),
                ('user_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
