# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-07 16:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0006_auto_20171001_1313'),
    ]

    operations = [
        migrations.AddField(
            model_name='electionsettings',
            name='loi_results_open',
            field=models.BooleanField(default=False),
        ),
    ]
