# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-07-31 00:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0036_comment_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='texto',
        ),
    ]