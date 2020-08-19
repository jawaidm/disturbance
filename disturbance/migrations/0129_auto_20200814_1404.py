# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2020-08-14 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0128_merge_20200810_1645'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiaryGlobalSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(choices=[('oracle_code_apiary_site_annural_rental_fee', 'Oracle code for the apiary site annual rental fee'), ('apiary_sites_list_token', 'Token to import the apiary sites list')], max_length=255, unique=True)),
                ('value', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Apiary Global Settings',
            },
        ),
        migrations.AlterModelOptions(
            name='sitecategory',
            options={'verbose_name': 'apiary site fee'},
        ),
        migrations.AlterField(
            model_name='globalsettings',
            name='key',
            field=models.CharField(choices=[('assessment_reminder_days', 'Assessment reminder days')], max_length=255, unique=True),
        ),
    ]
