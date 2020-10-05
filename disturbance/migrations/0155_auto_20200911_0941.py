# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-09-11 01:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0154_apiarysiteonapproval_wkb_geometry'),
    ]

    operations = [
        migrations.RenameField(
            model_name='approval',
            old_name='beehive_sites',
            new_name='apiary_sites',
        ),
        migrations.RenameField(
            model_name='proposalapiary',
            old_name='beehive_sites',
            new_name='apiary_sites',
        ),
        migrations.RemoveField(
            model_name='apiarysite',
            name='approval',
        ),
        migrations.RemoveField(
            model_name='apiarysite',
            name='proposal_apiaries',
        ),
        migrations.RemoveField(
            model_name='apiarysite',
            name='proposal_apiary',
        ),
    ]
