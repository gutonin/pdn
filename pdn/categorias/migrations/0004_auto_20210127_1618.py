# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-27 19:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0003_categoria_exibir_categoria'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='exibir_categoria',
            new_name='exibir_menu',
        ),
    ]
