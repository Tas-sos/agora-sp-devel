# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-30 07:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0016_auto_20200429_0358'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='pd_mri_1_description',
            field=models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name=b'PD.MRI.1_Description'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='pd_mri_2_logo',
            field=models.TextField(blank=True, default=None, null=True, verbose_name=b'PD.MRI.2_Logo'),
        ),
        migrations.AddField(
            model_name='organisation',
            name='pd_mri_3_multimedia',
            field=models.TextField(blank=True, default=None, null=True, verbose_name=b'PD.MRI.3_Multimedia'),
        ),
    ]
