# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-06 10:54
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0019_auto_20200505_1141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='pd_mri_1_description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default=None, max_length=100, null=True, verbose_name=b'PD.MRI.1_Description'),
        ),
    ]