# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-19 08:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=30, null=True, unique=True)),
                ('phone', models.CharField(max_length=30, null=True, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('token', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
    ]
