# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-13 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('chapeu', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=100)),
            ],
        ),
    ]
