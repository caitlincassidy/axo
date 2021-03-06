# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-01 15:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0003_auto_20170925_1758'),
    ]

    operations = [
        migrations.CreateModel(
            name='ElectionSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exec_election', models.BooleanField(default=False)),
                ('ois_open', models.BooleanField(default=False)),
                ('loi_open', models.BooleanField(default=False)),
                ('slating_open', models.BooleanField(default=False)),
                ('senior_class_year', models.IntegerField(default=2018)),
            ],
        ),
    ]
