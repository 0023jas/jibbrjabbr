# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-12-22 17:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jibbrjabbrmain', '0004_jjstory_storyimg'),
    ]

    operations = [
        migrations.CreateModel(
            name='storyReloadConditional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conditional', models.TextField()),
            ],
        ),
    ]
