# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-28 12:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20180125_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=b'static/assets/'),
        ),
    ]