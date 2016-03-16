# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-16 03:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forkship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Music',
            fields=[
                ('music_id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('track_id', models.AutoField(primary_key=True, serialize=False)),
                ('pathname', models.CharField(max_length=512)),
                ('music', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstreaming.Music')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=512)),
            ],
        ),
        migrations.AddField(
            model_name='music',
            name='users',
            field=models.ManyToManyField(through='musicstreaming.Forkship', to='musicstreaming.User'),
        ),
        migrations.AddField(
            model_name='forkship',
            name='music',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstreaming.Music'),
        ),
        migrations.AddField(
            model_name='forkship',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='musicstreaming.User'),
        ),
    ]
