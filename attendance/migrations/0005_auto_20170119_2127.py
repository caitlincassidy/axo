# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-20 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20170119_2039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='semester',
            options={'ordering': ['-year', 'term']},
        ),
    ]
