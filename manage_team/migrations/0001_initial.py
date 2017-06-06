# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(blank=True, max_length=10, null=True)),
                ('role', models.IntegerField(choices=[(0, 'Admin'), (1, 'Regular')], default=1)),
            ],
        ),
    ]
