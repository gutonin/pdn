# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2021-01-15 19:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import filebrowser.fields


class Migration(migrations.Migration):

    dependencies = [
        ('categorias', '0002_auto_20210114_1143'),
        ('redatores', '0001_initial'),
        ('tags', '0002_auto_20210113_1654'),
        ('artigos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artigo',
            name='categoria',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='data_publicacao',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='artigo',
            name='imagem',
            field=filebrowser.fields.FileBrowseField(blank=True, max_length=200, verbose_name='Image'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='redator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='redatores.Redator'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='artigo',
            name='tag',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tags.Tag'),
        ),
        migrations.AddField(
            model_name='artigo',
            name='texto',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='legenda',
            field=models.CharField(max_length=200),
        ),
    ]
