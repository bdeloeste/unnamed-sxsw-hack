# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 07:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicstreaming', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='music_name',
            field=models.CharField(default='', max_length=512),
        ),
    ]