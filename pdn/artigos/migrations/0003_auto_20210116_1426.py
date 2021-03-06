# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-16 17:26
from __future__ import unicode_literals

from django.db import migrations


def updateSlug(apps, schema_editor):
    art = apps.get_model('artigos', 'Artigo')
    valores = art.objects.all()
    for a in valores:
        a.save()


class Migration(migrations.Migration):

    dependencies = [
        ('artigos', '0002_auto_20210115_1604'),
    ]

    operations = [
        migrations.RunPython(updateSlug)
    ]
