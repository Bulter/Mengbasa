# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-01-20 17:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0005_rwm'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isselect', models.BooleanField(default=True)),
                ('number', models.IntegerField()),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Rwm')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.User')),
            ],
        ),
    ]