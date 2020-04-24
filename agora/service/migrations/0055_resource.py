# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-04-23 13:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_organisation_pd_bai_3_legal_entity'),
        ('service', '0054_auto_20190904_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('rd_bai_0_id', models.CharField(max_length=255, unique=True)),
                ('rd_bai_1_name', models.CharField(default=None, max_length=255)),
                ('rd_bai_4_webpage', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('rd_bai_2_organisation', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='organisation_services', to='accounts.Organisation')),
                ('rd_bai_3_providers', models.ManyToManyField(blank=True, related_name='provided_services', to='accounts.Organisation')),
            ],
        ),
    ]
