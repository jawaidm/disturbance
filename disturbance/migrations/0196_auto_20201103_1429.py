# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-11-03 06:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0195_proposalapiary_target_approval_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposalapiary',
            name='target_approval_expiry_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='proposalapiary',
            name='target_approval_start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
