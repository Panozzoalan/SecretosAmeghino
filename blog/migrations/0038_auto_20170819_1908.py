# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-08-19 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20170730_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.CharField(max_length=10),
        ),
    ]