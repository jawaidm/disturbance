# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-07-10 06:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0107_merge_20200709_1120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apiarysitefeetype',
            name='name',
            field=models.CharField(choices=[('new_application', 'New Application'), ('transfer', 'Transfer')], max_length=50, unique=True),
        ),
    ]
