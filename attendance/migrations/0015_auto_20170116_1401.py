# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-16 19:01
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0014_auto_20170116_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excuse',
            name='text',
            field=models.CharField(max_length=1000, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
