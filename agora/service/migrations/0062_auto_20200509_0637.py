# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2020-05-09 06:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0026_merge_20200508_1306'),
        ('service', '0061_auto_20200507_1137'),
    ]

    operations = [
        migrations.AddField(
            model_name='resource',
            name='rd_cli_1_scientific_domain',
            field=models.ManyToManyField(blank=True, related_name='domain_resources', to='accounts.Domain', verbose_name='RD.CLI.1 Scientific Domain'),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_cli_2_scientific_subdomain',
            field=models.ManyToManyField(blank=True, related_name='subdomain_resources', to='accounts.Subdomain', verbose_name='RD.CLI.2 Scientific Subdomain'),
        ),
        migrations.AddField(
            model_name='resource',
            name='rd_cli_5_tags',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='RD.CLI.5 Scientific Subdomain'),
        ),
    ]
