# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-27 19:16
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0004_artigo_exibir_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artigo',
            name='exibir_menu',
        ),
    ]
