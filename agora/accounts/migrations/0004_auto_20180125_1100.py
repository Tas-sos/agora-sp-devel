# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-25 11:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[['observer', 'Observer'], ['serviceowner', 'Service Owner'], ['admin', 'Admin'], ['superadmin', 'Superadmin']], default=b'observer', max_length=20),
        ),
    ]
