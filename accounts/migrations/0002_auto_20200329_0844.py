# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-03-29 08:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='telephone',
            field=models.IntegerField(default=''),
        ),
    ]